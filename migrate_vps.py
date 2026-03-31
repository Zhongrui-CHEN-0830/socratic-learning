import paramiko, time, sys, json
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

# Read env to get Supabase credentials
env = cmd('cat /opt/socratic-learning/server/.env', 3)
print('=== ENV ===')
print(env[:500])

# Parse SUPABASE_URL and SUPABASE_SERVICE_KEY
supabase_url = ''
service_key = ''
for line in env.splitlines():
    if line.startswith('SUPABASE_URL='):
        supabase_url = line.split('=', 1)[1].strip()
    elif line.startswith('SUPABASE_SERVICE_KEY='):
        service_key = line.split('=', 1)[1].strip()

print(f'URL: {supabase_url}')
print(f'Key: {service_key[:20]}...')

# Execute SQL via Supabase REST API
sql1 = "alter table public.api_keys add column if not exists model text;"
sql2 = "alter table public.api_keys drop constraint if exists api_keys_provider_check;"

for sql in [sql1, sql2]:
    curl_cmd = f"""curl -s -X POST '{supabase_url}/rest/v1/rpc/exec_sql' \
  -H 'apikey: {service_key}' \
  -H 'Authorization: Bearer {service_key}' \
  -H 'Content-Type: application/json' \
  -d '{{"query": "{sql}"}}' 2>&1"""
    # Use Supabase SQL endpoint instead
    # Actually use the pg REST endpoint
    pass

# Use psql via supabase CLI or direct pg connection
# Check if psql is available
print('\n=== Check psql ===')
print(cmd('which psql 2>&1 || echo "no psql"', 3))

# Try using supabase CLI
print('\n=== Check supabase CLI ===')
print(cmd('which supabase 2>&1 || echo "no supabase"', 3))

# Use curl to call Supabase SQL API directly
print('\n=== Execute migration via Supabase SQL API ===')
migration_sql = "alter table public.api_keys add column if not exists model text; alter table public.api_keys drop constraint if exists api_keys_provider_check;"

curl_cmd = f"""curl -s -X POST '{supabase_url}/rest/v1/rpc/exec' \
  -H 'apikey: {service_key}' \
  -H 'Authorization: Bearer {service_key}' \
  -H 'Content-Type: application/json' \
  -d '{json.dumps({"query": migration_sql})}' 2>&1"""
print(cmd(curl_cmd, 8))

client.close()
print('DONE')
