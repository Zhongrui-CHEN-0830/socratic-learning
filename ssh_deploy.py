import paramiko, time, sys, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=10, auth_timeout=10)
client.get_transport().set_keepalive(5)

def run(cmd, wait=8):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=30)
    time.sleep(wait)
    return (stdout.read() + stderr.read()).decode('utf-8', errors='replace')

print("--- Frontend npm install ---")
print(run('cd /opt/socratic-learning/frontend && npm install 2>&1', 20)[:200])

print("\n--- Frontend build ---")
result = run('cd /opt/socratic-learning/frontend && npm run build 2>&1', 60)
print("build result:", result[:400])

print("\n--- Check dist ---")
print(run('ls /opt/socratic-learning/frontend/dist/ 2>&1', 3))

print("\n--- Root HTTP (after frontend) ---")
code = run('curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000/ 2>&1', 5)
print("http:", code)

# Check if it serves HTML
html = run('curl -s --max-time 5 http://127.0.0.1:3000/ 2>&1', 8)
print("HTML sample:", html[:200])

client.close()
print("\n=== DONE ===")
