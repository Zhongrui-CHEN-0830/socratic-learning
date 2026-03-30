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

print("--- chat.js LAST 5 lines ---")
print(run('tail -5 /opt/socratic-learning/server/dist/routes/chat.js 2>&1', 5))

print("--- chat.js file size ---")
print(run('wc -l /opt/socratic-learning/server/dist/routes/chat.js 2>&1', 3))

print("--- check for 'export' in chat.js ---")
print(run('grep -n "export" /opt/socratic-learning/server/dist/routes/chat.js 2>&1', 3))

print("--- dist/routes/ contents ---")
print(run('ls /opt/socratic-learning/server/dist/routes/ 2>&1', 3))

client.close()
