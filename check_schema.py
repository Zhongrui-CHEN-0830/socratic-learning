import paramiko, time, sys, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)

def cmd(c, wait=8):
    chan = client.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    out = chan.recv(65536).decode('utf-8', errors='replace')
    err = chan.recv_stderr(16384).decode('utf-8', errors='replace')
    return out + err

# Read env
env = cmd('cat /opt/socratic-learning/server/.env', 3)
supabase_url = ''
service_key = ''
for line in env.splitlines():
    if line.startswith('SUPABASE_URL='):
        supabase_url = line.split('=', 1)[1].strip()
    elif line.startswith('SUPABASE_SERVICE_KEY='):
        service_key = line.split('=', 1)[1].strip()

# Test if model column exists via REST API
print('=== Check model column via REST ===')
check_cmd = f"curl -s '{supabase_url}/rest/v1/api_keys?select=id,model&limit=1' -H 'apikey: {service_key}' -H 'Authorization: Bearer {service_key}'"
print(cmd(check_cmd, 8))

# Test if provider constraint allows deepseek
print('\n=== Check provider constraint ===')
# Try to select with a filter that would fail if constraint is strict
check2 = f"curl -s '{supabase_url}/rest/v1/api_keys?select=id,provider&limit=1' -H 'apikey: {service_key}' -H 'Authorization: Bearer {service_key}'"
print(cmd(check2, 8))

client.close()
print('DONE')
