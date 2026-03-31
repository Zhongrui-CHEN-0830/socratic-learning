import paramiko, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)

def cmd(c, wait=5):
    chan = client.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    out = chan.recv(16384).decode('utf-8', errors='replace')
    err = chan.recv_stderr(16384).decode('utf-8', errors='replace')
    return out + err

print('=== dist/routes/ ===')
print(cmd('ls -la /opt/socratic-learning/server/dist/routes/', 3))

print('\n=== dist/routes/auth.js ===')
print(cmd('cat /opt/socratic-learning/server/dist/routes/auth.js', 3))

print('\n=== Full PM2 error log (last 50 lines) ===')
print(cmd('tail -50 /root/.pm2/logs/socratic-learning-error.log 2>&1', 3))

print('\n=== PM2 out log (last 20 lines) ===')
print(cmd('tail -20 /root/.pm2/logs/socratic-learning-out.log 2>&1', 3))

client.close()
print('DONE')
