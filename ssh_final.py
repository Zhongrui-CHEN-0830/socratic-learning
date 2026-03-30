import paramiko, time, sys
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

print("1. PM2:", cmd('pm2 list', 3)[:200])
print("\n2. Health:", cmd('curl -s http://127.0.0.1:3000/api/health', 5))
print("\n3. Website title:", cmd("curl -s http://127.0.0.1:3000/ | grep '<title>'", 8)[:100])
print("\n4. TypeScript compile:", cmd('cd /opt/socratic-learning/server && npx tsc 2>&1', 30)[:300])

client.close()
print("\n✅ 部署完成！网站: http://23.27.48.187")
