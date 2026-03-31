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

# Check what VITE_SUPABASE_URL is baked into the bundle
print('=== Check if placeholder supabase URL is in bundle ===')
print(cmd("grep -o 'placeholder.supabase.co' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1", 5))

# Check if undefined is in the bundle for supabase
print('\n=== Check createClient call in bundle ===')
print(cmd("grep -o 'createClient([^)]*' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -5", 5))

# Check if there's a supabaseUrl variable in the bundle
print('\n=== Check supabaseUrl in bundle ===')
print(cmd("grep -o 'supabaseUrl[^,;]*' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -5", 5))

# Check if the bundle has any error about supabase
print('\n=== Check for supabase error handling in bundle ===')
print(cmd("grep -o 'supabaseUrl.*undefined\\|Invalid URL\\|supabase.*error' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -5", 5))

# Check what the frontend was built with - look for env vars
print('\n=== Check env vars baked into bundle ===')
print(cmd("grep -o 'VITE_[A-Z_]*[^\"]*' /opt/socratic-learning/frontend/dist/assets/index-H33zXL_6.js 2>&1 | head -10", 5))

client.close()
print('DONE')
