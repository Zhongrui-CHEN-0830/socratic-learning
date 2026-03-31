import paramiko, time, sys, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)
client.get_transport().set_keepalive(5)
print("connected")

def cmd(c, wait=8):
    chan = client.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    return chan.recv(16384).decode('utf-8', errors='replace')

print("1. Git pull...")
print(cmd('cd /opt/socratic-learning && git pull origin main', 10)[:200])

print("\n2. TypeScript compile...")
print(cmd('cd /opt/socratic-learning/server && rm -rf dist && npx tsc 2>&1', 30)[:400])

print("\n3. Restart PM2...")
print(cmd('pm2 restart socratic-learning', 8)[:200])

print("\n4. Wait 8s...")
time.sleep(8)

print("\n5. Health:", cmd('curl -s http://127.0.0.1:3000/api/health', 5))

print("\n6. Test register via API:")
print(cmd('curl -s -X POST http://127.0.0.1:3000/api/auth/register -H "Content-Type: application/json" -d \'{"email":"test@test.com","password":"testpassword123"}\' 2>&1', 8)[:300])

client.close()
print("\nDONE")
