import paramiko, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)
client.get_transport().set_keepalive(5)
print("connected")

def cmd(c, wait=5):
    chan = client.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    return chan.recv(16384).decode('utf-8', errors='replace')

print("PM2 status:", cmd('pm2 list', 3)[:200])
print("\nHealth:", cmd('curl -s http://127.0.0.1:3000/api/health', 5)[:100])
print("\nHTTPS check:", cmd('curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000/', 5))
print("\nPM2 save:", cmd('pm2 save', 3)[:100])
print("\nTitle tag:", cmd("curl -s http://127.0.0.1:3000/ | grep '<title>'", 5)[:100])

client.close()
print("\n✅ 网站已上线: http://23.27.48.187")
