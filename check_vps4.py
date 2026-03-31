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

# Check what frontend dist has for API calls
print('=== Frontend dist - check for API calls ===')
print(cmd('grep -r "api/auth\|apiFetch\|Content-Type" /opt/socratic-learning/frontend/dist/assets/*.js 2>&1 | head -20', 5))

# Check if frontend dist exists
print('\n=== Frontend dist files ===')
print(cmd('ls -la /opt/socratic-learning/frontend/dist/assets/ 2>&1 | head -20', 3))

# Test with verbose curl to see what's happening
print('\n=== Verbose test register (check request/response) ===')
test_cmd = "curl -v -X POST http://127.0.0.1:3000/api/auth/register -H 'Content-Type: application/json' -d '{\"email\":\"newtest2@example.com\",\"password\":\"testpass123\"}' 2>&1"
print(cmd(test_cmd, 8))

# Check if there's a newer error in the log
print('\n=== Latest PM2 error log (last 10 lines) ===')
print(cmd('tail -10 /root/.pm2/logs/socratic-learning-error.log 2>&1', 3))

client.close()
print('DONE')
