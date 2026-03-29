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

# 1. Delete old dist to avoid conflicts
print("--- delete old dist ---")
print(run('rm -rf /opt/socratic-learning/server/dist', 3))

# 2. Try tsx directly (no tsc needed)
print("--- install tsx locally ---")
print(run('cd /opt/socratic-learning/server && npm install tsx 2>&1', 15))

# 3. Start with node directly via tsx (don't use pm2 with tsx - use node directly)
print("--- test run tsx ---")
print(run('cd /opt/socratic-learning/server && timeout 10 npx tsx index.ts 2>&1', 12))

c.close()
print("DONE")
