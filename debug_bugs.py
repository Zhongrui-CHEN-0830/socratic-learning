import paramiko, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)

def cmd(c, wait=6):
    chan = client.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    out = chan.recv(65536).decode('utf-8', errors='replace')
    err = chan.recv_stderr(16384).decode('utf-8', errors='replace')
    return out + err

# 1. Check PM2 error log for recent errors
print('=== 1. PM2 error log (last 30) ===')
print(cmd('tail -30 /root/.pm2/logs/socratic-learning-error.log 2>&1', 4))

# 2. Check PM2 out log (last 10)
print('\n=== 2. PM2 out log (last 10) ===')
print(cmd('tail -10 /root/.pm2/logs/socratic-learning-out.log 2>&1', 4))

# 3. Test health
print('\n=== 3. Health ===')
print(cmd('curl -s http://127.0.0.1:3000/api/health', 4))

# 4. Test login
print('\n=== 4. Test login ===')
login = cmd("curl -s -X POST http://127.0.0.1:3000/api/auth/login -H 'Content-Type: application/json' -d '{\"email\":\"test@example.com\",\"password\":\"testpass123\"}'", 8)
print(login[:500])

# Extract token
import re
m = re.search(r'"token":"([^"]+)"', login)
if m:
    token = m.group(1)
    print(f'\nGot token: {token[:30]}...')
    
    # 5. Get user's API keys
    print('\n=== 5. Get API keys ===')
    print(cmd(f"curl -s http://127.0.0.1:3000/api/user/api-keys -H 'Authorization: Bearer {token}'", 6))
    
    # 6. Get conversations
    print('\n=== 6. Get conversations ===')
    print(cmd(f"curl -s http://127.0.0.1:3000/api/conversations -H 'Authorization: Bearer {token}'", 6))

client.close()
print('\nDONE')
