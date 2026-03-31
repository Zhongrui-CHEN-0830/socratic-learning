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

# Simulate exactly what the browser would send
print('=== Simulate browser request (with Origin header) ===')
test_cmd = """curl -v -X POST http://23.27.48.187:80/api/auth/register \
  -H 'Content-Type: application/json' \
  -H 'Origin: http://23.27.48.187' \
  -H 'Referer: http://23.27.48.187/register' \
  -d '{"email":"browsertest@example.com","password":"testpass123"}' 2>&1"""
print(cmd(test_cmd, 10))

print('\n=== Test login with same approach ===')
login_cmd = """curl -s -X POST http://23.27.48.187:80/api/auth/login \
  -H 'Content-Type: application/json' \
  -H 'Origin: http://23.27.48.187' \
  -d '{"email":"browsertest@example.com","password":"testpass123"}' 2>&1"""
print(cmd(login_cmd, 10))

# Check if there are any new errors in the log
print('\n=== Check for new errors after our tests ===')
print(cmd('tail -5 /root/.pm2/logs/socratic-learning-error.log 2>&1', 3))

# Check the frontend dist for any hardcoded API URL
print('\n=== Check for hardcoded API URL in frontend ===')
print(cmd("grep -o 'http://[^\"]*api[^\"]*' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -5", 5))

client.close()
print('DONE')
