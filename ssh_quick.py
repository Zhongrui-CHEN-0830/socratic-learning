import paramiko, time
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=10)
stdin, stdout, stderr = client.exec_command('tail -30 /root/.pm2/logs/socratic-learning-error.log')
time.sleep(3)
out = stdout.read()
print(out.decode('utf-8', errors='replace'))
client.close()
