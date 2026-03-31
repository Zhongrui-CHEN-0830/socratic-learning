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

# Search for apiFetch and auth-related code in the frontend bundle
print('=== Search for apiFetch in frontend bundle ===')
print(cmd('grep -o "apiFetch[^;]*" /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -20', 5))

print('\n=== Search for /api/auth in frontend bundle ===')
print(cmd('grep -o "/api/auth[^\"]*" /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -20', 5))

print('\n=== Search for Content-Type in frontend bundle ===')
print(cmd('grep -o "Content-Type[^,}]*" /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -10', 5))

# Check if there's a VITE_SUPABASE_URL in the bundle (should be baked in at build time)
print('\n=== Check if Supabase URL is baked into frontend bundle ===')
print(cmd('grep -o "supabase.co[^\"]*" /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -5', 5))

# Check the frontend .env.example
print('\n=== frontend .env.example ===')
print(cmd('cat /opt/socratic-learning/frontend/.env.example 2>&1 || cat /opt/socratic-learning/frontend/.env.local 2>&1 || echo "no env files"', 3))

# Check git log to see what changed recently
print('\n=== Recent git log ===')
print(cmd('cd /opt/socratic-learning && git log --oneline -10 2>&1', 3))

client.close()
print('DONE')
