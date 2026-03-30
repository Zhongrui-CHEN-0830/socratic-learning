import paramiko, time, sys, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=10, auth_timeout=10)
client.get_transport().set_keepalive(5)

def run(cmd, wait=5):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=20)
    time.sleep(wait)
    return (stdout.read() + stderr.read()).decode('utf-8', errors='replace')

# 1. Check what's actually in the server dist (old placeholder)
print("--- server dist/index.html (old placeholder) ---")
print(run('head -8 /opt/socratic-learning/server/dist/index.html 2>&1', 3))

# 2. Check where the frontend dist is  
print("\n--- Frontend dist ---")
print(run('head -8 /opt/socratic-learning/frontend/dist/index.html 2>&1', 3))

# 3. Check PM2 restart
print("\n--- Restart PM2 with latest code ---")
print(run('pm2 restart socratic-learning 2>&1', 8))
time.sleep(5)

print("\n--- Health after restart ---")
print(run('curl -s http://127.0.0.1:3000/api/health 2>&1', 5))

print("\n--- Root HTTP after restart ---")
code = run('curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000/ 2>&1', 5)
print("HTTP:", code)

html = run('curl -s --max-time 5 http://127.0.0.1:3000/ 2>&1', 8)
print("HTML:", html[:300])

client.close()
print("\nDONE")
