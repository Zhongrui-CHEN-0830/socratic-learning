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
    out = chan.recv(65536).decode('utf-8', errors='replace')
    err = chan.recv_stderr(16384).decode('utf-8', errors='replace')
    return out + err

# Search for auth-related strings in the bundle
print('=== Search for auth/login in frontend bundle ===')
print(cmd("grep -o 'auth/login[^,]*' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -10", 5))

print('\n=== Search for auth/register in frontend bundle ===')
print(cmd("grep -o 'auth/register[^,]*' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -10", 5))

# Check if supabase URL is in the bundle
print('\n=== Check supabase in bundle ===')
print(cmd("grep -o 'uxtmvcextmbxdfwolpek[^\"]*' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -5", 5))

# Check if VITE env vars are undefined in bundle
print('\n=== Check VITE env vars in bundle ===')
print(cmd("grep -o 'VITE_[A-Z_]*' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -10", 5))

# Check what the frontend .env was at build time
print('\n=== Check frontend .env in git ===')
print(cmd("cd /opt/socratic-learning && git show HEAD:frontend/.env 2>&1 || echo 'not in git'", 3))

# Check if there's a .env in the frontend dir
print('\n=== All files in frontend dir ===')
print(cmd("ls -la /opt/socratic-learning/frontend/ 2>&1", 3))

client.close()
print('DONE')
