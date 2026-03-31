import paramiko, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)

def cmd(c, wait=6):
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

# 1. Verify model column exists
print('=== 1. model column exists? ===')
r = cmd(f"curl -s '{supabase_url}/rest/v1/api_keys?select=id,model&limit=1' -H 'apikey: {service_key}' -H 'Authorization: Bearer {service_key}'", 6)
print(r[:200])

# 2. Verify provider constraint is gone (try inserting deepseek)
print('\n=== 2. provider constraint removed? ===')
import json
payload = json.dumps({
    "user_id": "98067e3f-36d8-4d42-a73a-72f7d4ca3b81",
    "provider": "deepseek",
    "base_url": "https://api.deepseek.com/v1",
    "encrypted_key": "test",
    "iv": "test",
    "model": "deepseek-chat",
    "is_active": False
})
r2 = cmd(f"curl -s -X POST '{supabase_url}/rest/v1/api_keys' -H 'apikey: {service_key}' -H 'Authorization: Bearer {service_key}' -H 'Content-Type: application/json' -H 'Prefer: return=minimal' -d '{payload}'", 6)
print('Response:', r2[:200] if r2.strip() else '(empty = success)')

# 3. Test save API key via app endpoint
print('\n=== 3. Test save API key via /api/user/api-keys ===')
# First login to get token
login = cmd("curl -s -X POST http://127.0.0.1:3000/api/auth/login -H 'Content-Type: application/json' -d '{\"email\":\"deploy_test@example.com\",\"password\":\"testpass123\"}'", 8)
import re
token_match = re.search(r'"token":"([^"]+)"', login)
if token_match:
    token = token_match.group(1)
    print(f'Got token: {token[:30]}...')
    
    # Save a deepseek key
    save_cmd = f"""curl -s -X POST http://127.0.0.1:3000/api/user/api-keys \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {token}' \
  -d '{{"provider":"deepseek","base_url":"https://api.deepseek.com/v1","key":"sk-test-key-123","model":"deepseek-chat"}}'"""
    r3 = cmd(save_cmd, 8)
    print('Save result:', r3[:300])
else:
    print('Login failed:', login[:200])

client.close()
print('\nDONE')
