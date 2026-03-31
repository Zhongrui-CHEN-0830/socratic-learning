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
    return chan.recv(16384).decode('utf-8', errors='replace')

print("=== tsconfig.json ===")
print(cmd('cat /opt/socratic-learning/server/tsconfig.json', 3))

print("\n=== package.json type ===")
print(cmd('grep -E "type|module" /opt/socratic-learning/server/package.json', 3))

print("\n=== dist/index.js first 5 lines ===")
print(cmd('head -5 /opt/socratic-learning/server/dist/index.js', 3))

client.close()
