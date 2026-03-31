import paramiko, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)

def cmd(c, wait=5):
    chan = client.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    out = chan.recv(65536).decode('utf-8', errors='replace')
    err = chan.recv_stderr(16384).decode('utf-8', errors='replace')
    return out + err

# Test through nginx (port 80) to simulate real user
print('=== Test register through nginx (port 80) ===')
test_cmd = "curl -s -X POST http://127.0.0.1:80/api/auth/register -H 'Content-Type: application/json' -d '{\"email\":\"nginxtest@example.com\",\"password\":\"testpass123\"}'"
print(cmd(test_cmd, 8))

print('\n=== Test login through nginx (port 80) ===')
login_cmd = "curl -s -X POST http://127.0.0.1:80/api/auth/login -H 'Content-Type: application/json' -d '{\"email\":\"nginxtest@example.com\",\"password\":\"testpass123\"}'"
print(cmd(login_cmd, 8))

# Check if there's a newer error after our tests
print('\n=== Latest error log timestamp ===')
print(cmd('tail -5 /root/.pm2/logs/socratic-learning-error.log 2>&1', 3))

# Check if the frontend dist has the correct Auth.module.css
print('\n=== Check if Auth.module.css exists in dist ===')
print(cmd('ls /opt/socratic-learning/frontend/dist/assets/ 2>&1', 3))

# Check if there's a CSS module issue
print('\n=== Check frontend src for Auth.module.css ===')
print(cmd('ls /opt/socratic-learning/frontend/src/pages/ 2>&1', 3))

client.close()
print('DONE')
