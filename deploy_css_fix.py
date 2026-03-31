import paramiko, time, sys
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

print('=== 1. Git pull ===')
print(cmd('cd /opt/socratic-learning && git pull origin main 2>&1', 8))

print('\n=== 2. Rebuild frontend ===')
result = cmd('cd /opt/socratic-learning/frontend && npm run build 2>&1', 60)
print(result[-300:])

print('\n=== 3. Verify CSS no longer has googleapis ===')
print(cmd('head -c 200 /opt/socratic-learning/frontend/dist/assets/index-*.css', 3))

print('\n=== 4. Restart PM2 ===')
print(cmd('pm2 restart socratic-learning 2>&1 | tail -5', 5))

print('\n=== 5. Health check ===')
print(cmd('curl -s http://127.0.0.1:3000/api/health', 5))

client.close()
print('\nDONE')
