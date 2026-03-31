import paramiko, time, sys
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

# Get user list to find the actual user
print('=== 1. Get users ===')
users = cmd('curl -s "https://uxtmvcextmbxdfwolpek.supabase.co/rest/v1/users?select=id,email" -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio"', 10)
print(users[:1000])

# Try to find the API key for the user
# First, let me check the api_keys table
print('\n=== 2. Get all API keys ===')
keys = cmd('curl -s "https://uxtmvcextmbxdfwolpek.supabase.co/rest/v1/api_keys?select=id,provider,base_url,model,is_active" -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio"', 10)
print(keys)

# Check character_states for the user
print('\n=== 3. Get character_states ===')
states = cmd('curl -s "https://uxtmvcextmbxdfwolpek.supabase.co/rest/v1/character_states?select=*" -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio"', 10)
print(states[:1000])

# Check conversations for the user
print('\n=== 4. Get conversations ===')
convs = cmd('curl -s "https://uxtmvcextmbxdfwolpek.supabase.co/rest/v1/conversations?select=*" -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio" -H "Prefer: count=exact"', 10)
print(convs[:2000])

client.close()
print('\nDONE')