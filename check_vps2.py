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

print('=== Check compiled index.js for express.json on /api/auth ===')
print(cmd('grep -n "api/auth\|express.json\|json(" /opt/socratic-learning/server/dist/index.js | head -30', 3))

print('\n=== Check if dist exists and when compiled ===')
print(cmd('ls -la /opt/socratic-learning/server/dist/ 2>&1 | head -20', 3))

print('\n=== PM2 status ===')
print(cmd('pm2 list 2>&1', 3))

print('\n=== Check frontend .env on VPS ===')
print(cmd('cat /opt/socratic-learning/frontend/.env 2>&1', 3))

print('\n=== Check nginx config ===')
print(cmd('cat /etc/nginx/sites-enabled/default 2>&1 || cat /etc/nginx/nginx.conf 2>&1 | head -50', 3))

client.close()
print('DONE')
