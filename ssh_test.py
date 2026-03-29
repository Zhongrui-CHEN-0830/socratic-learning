import paramiko, time, sys, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(host, port=port, username=user, password=pw, timeout=10)

def run(cmd, wait=5):
    stdin, stdout, stderr = c.exec_command(cmd)
    time.sleep(wait)
    out = stdout.read(); err = stderr.read()
    return (out+err).decode('utf-8', errors='replace')

# 1. Pull latest
print("--- git pull ---")
print(run('cd /opt/socratic-learning && git pull origin main', 10)[:300])

# 2. Install tsx locally
print("--- install tsx ---")
print(run('cd /opt/socratic-learning/server && npm install tsx --save-dev', 15)[:200])

# 3. Kill old pm2
print("--- delete old pm2 ---")
print(run('pm2 delete socratic-learning 2>/dev/null; true', 3))

# 4. Compile tsx
print("--- tsc ---")
result = run('cd /opt/socratic-learning/server && npx tsc 2>&1', 20)
print("tsc result:", result[:500])

# 5. Check if dist/index.js exists
print("--- dist check ---")
print(run('ls -la /opt/socratic-learning/server/dist/index.js 2>&1', 3))

# 6. Start with node directly (compiled dist)
print("--- start pm2 with node ---")
result = run('cd /opt/socratic-learning/server && pm2 start dist/index.js --name socratic-learning 2>&1', 8)
print(result[:300])

# 7. Save
print("--- pm2 save ---")
print(run('pm2 save 2>&1', 3))
print(run('pm2 startup 2>&1 || true', 5))

# 8. Wait and check
time.sleep(5)
print("--- health ---")
print(run('curl -s --max-time 5 http://127.0.0.1:3000/api/health 2>&1', 8))

print("--- http status ---")
print(run('curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000/ 2>&1', 5))

print("--- pm2 logs ---")
print(run('pm2 logs --lines 15 --nostream 2>&1', 5))

c.close()
print("DONE")
