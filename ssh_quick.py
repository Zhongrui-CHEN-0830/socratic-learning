import paramiko, time
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)
print("connected")
# PM2 logs
stdin, stdout, stderr = client.exec_command('pm2 logs --lines 20 --err --nostream 2>&1')
time.sleep(10)
print("LOGS:", stdout.read().decode('utf-8', errors='replace'))
client.close()
