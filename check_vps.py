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
    out = chan.recv(16384).decode('utf-8', errors='replace')
    err = chan.recv_stderr(16384).decode('utf-8', errors='replace')
    return out + err

print('=== VPS server .env ===')
print(cmd('cat /opt/socratic-learning/server/.env 2>&1 || echo NOT_FOUND', 3))

print('\n=== PM2 error log (last 30 lines) ===')
print(cmd('tail -30 /root/.pm2/logs/socratic-learning-error.log 2>&1', 3))

print('\n=== Test register API ===')
test_cmd = "curl -s -X POST http://127.0.0.1:3000/api/auth/register -H 'Content-Type: application/json' -d '{\"email\":\"test@example.com\",\"password\":\"testpass123\"}'"
print(cmd(test_cmd, 8))

print('\n=== Test login API ===')
login_cmd = "curl -s -X POST http://127.0.0.1:3000/api/auth/login -H 'Content-Type: application/json' -d '{\"email\":\"test@example.com\",\"password\":\"testpass123\"}'"
print(cmd(login_cmd, 8))

client.close()
print('DONE')
