import paramiko, time, sys, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)

def cmd(c, wait=8):
    chan = client.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    out = chan.recv(65536).decode('utf-8', errors='replace')
    err = chan.recv_stderr(16384).decode('utf-8', errors='replace')
    return out + err

# Step 1: Git pull latest code
print('=== 1. Git pull ===')
print(cmd('cd /opt/socratic-learning && git fetch origin main && git reset --hard origin/main 2>&1', 12))

# Step 2: Rebuild server TypeScript
print('\n=== 2. Rebuild server ===')
result = cmd('cd /opt/socratic-learning/server && rm -rf dist && npx tsc 2>&1', 30)
if 'error TS' in result:
    print('TSC ERRORS:', result[:800])
else:
    print('TSC OK:', result[:200] if result.strip() else '(no output = success)')

# Step 3: Rebuild frontend
print('\n=== 3. Rebuild frontend ===')
result2 = cmd('cd /opt/socratic-learning/frontend && npm run build 2>&1', 60)
if 'error' in result2.lower() and 'Error' in result2:
    print('BUILD ERRORS:', result2[:800])
else:
    print('Frontend build:', result2[-300:])

# Step 4: Restart PM2
print('\n=== 4. Restart PM2 ===')
print(cmd('pm2 restart socratic-learning 2>&1', 8))

time.sleep(5)

# Step 5: Health check
print('\n=== 5. Health check ===')
print(cmd('curl -s http://127.0.0.1:3000/api/health', 5))

# Step 6: Test register
print('\n=== 6. Test register ===')
print(cmd("curl -s -X POST http://127.0.0.1:3000/api/auth/register -H 'Content-Type: application/json' -d '{\"email\":\"deploy_test@example.com\",\"password\":\"testpass123\"}'", 8))

client.close()
print('\nDONE')
