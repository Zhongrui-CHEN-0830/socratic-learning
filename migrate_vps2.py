import paramiko, time, sys, json, re
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

# Extract project ref from URL (e.g. uxtmvcextmbxdfwolpek)
project_ref = supabase_url.replace('https://', '').split('.')[0]
print(f'Project ref: {project_ref}')

# Use Supabase Management API to run SQL
# POST https://api.supabase.com/v1/projects/{ref}/database/query
# But this requires a personal access token, not service key

# Alternative: use the pg connection string via node
# Let's write a small Node.js script to run the migration
migration_script = """
const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_KEY
);

async function migrate() {
  // Try to add model column by inserting a test row with model field
  // If column doesn't exist, we'll get an error
  
  // Check if model column exists
  const { data, error } = await supabase
    .from('api_keys')
    .select('model')
    .limit(1);
  
  if (error && error.message.includes('model')) {
    console.log('model column does not exist, need to add it');
    console.log('ERROR:', error.message);
  } else {
    console.log('model column already exists or no rows');
  }
}

migrate().catch(console.error);
"""

# Write and run the check script
import io
sftp = client.open_sftp()
sftp.putfo(io.BytesIO(migration_script.encode('utf-8')), '/tmp/check_model.js')
sftp.close()

print('\n=== Check if model column exists ===')
print(cmd('cd /opt/socratic-learning/server && node /tmp/check_model.js', 10))

# Now try to add the column via a direct insert with model field
# If it fails with "column does not exist", we know we need to add it
test_script = """
const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_KEY
);

async function test() {
  // Try selecting model column
  const { data, error } = await supabase
    .from('api_keys')
    .select('id, provider, model')
    .limit(1);
  
  if (error) {
    console.log('SELECT model error:', JSON.stringify(error));
  } else {
    console.log('SELECT model OK, data:', JSON.stringify(data));
  }
  
  // Try to get provider constraint info
  const { data: d2, error: e2 } = await supabase
    .from('api_keys')
    .insert({
      user_id: '00000000-0000-0000-0000-000000000000',
      provider: 'deepseek',
      base_url: 'test',
      encrypted_key: 'test',
      iv: 'test',
      is_active: false
    });
  console.log('INSERT deepseek provider:', e2 ? JSON.stringify(e2) : 'OK');
}

test().catch(console.error);
"""

sftp = client.open_sftp()
sftp.putfo(io.BytesIO(test_script.encode('utf-8')), '/tmp/test_schema.js')
sftp.close()

print('\n=== Test schema ===')
print(cmd('cd /opt/socratic-learning/server && node /tmp/test_schema.js', 10))

client.close()
print('DONE')
