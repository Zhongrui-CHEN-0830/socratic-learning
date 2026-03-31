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
    return chan.recv(16384).decode('utf-8', errors='replace')

print("=== Test Register ===")
print(cmd('curl -s -X POST http://127.0.0.1:3000/api/auth/register -H "Content-Type: application/json" -d \'{"email":"testuser@example.com","password":"testpassword123"}\'', 10)[:400])

print("\n=== PM2 Errors (last 5) ===")
print(cmd('tail -5 /root/.pm2/logs/socratic-learning-error.log 2>&1', 5)[:600])

print("\n=== PM2 Status ===")
print(cmd('pm2 jlist socratic-learning 2>&1 | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[0][\"pm2_env\"][\"status\"])"', 8))

client.close()
print("\nDONE")
