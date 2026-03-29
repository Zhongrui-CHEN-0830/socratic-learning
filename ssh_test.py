import paramiko, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=10, auth_timeout=10)
client.get_transport().set_keepalive(5)
print("connected")

def run(cmd, wait=8):
    try:
        stdin, stdout, stderr = client.exec_command(cmd, timeout=15)
        time.sleep(wait)
        result = (stdout.read() + stderr.read()).decode('utf-8', errors='replace')
        return result
    except Exception as e:
        return f"ERROR: {e}"

print("--- git pull ---")
print(run('cd /opt/socratic-learning && git pull origin main', 10)[:400])

print("--- tsc ---")
print(run('cd /opt/socratic-learning/server && npx tsc 2>&1', 20)[:400])

print("--- check dist ---")
print(run('ls /opt/socratic-learning/server/dist/ 2>&1', 3))

print("--- pm2 restart ---")
print(run('pm2 delete socratic-learning 2>/dev/null; true', 3))
print(run('cd /opt/socratic-learning/server && pm2 start dist/index.js --name socratic-learning 2>&1', 8)[:300])

print("--- wait 5s then check ---")
time.sleep(5)

print("--- health ---")
print(run('curl -s --max-time 5 http://127.0.0.1:3000/api/health 2>&1', 8))

print("--- pm2 logs ---")
print(run('pm2 logs --lines 10 --nostream 2>&1', 5))

client.close()
print("DONE")
