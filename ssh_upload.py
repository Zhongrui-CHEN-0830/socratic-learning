import paramiko, time, sys, io, os, glob
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
local_dist = r'C:\Users\29539\socratic-learning\frontend\dist'
remote_dist = '/opt/socratic-learning/frontend/dist'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=10, auth_timeout=10)
client.get_transport().set_keepalive(5)
sftp = client.open_sftp()
print("SFTP connected!")

def run(cmd, wait=5):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=20)
    time.sleep(wait)
    return (stdout.read() + stderr.read()).decode('utf-8', errors='replace')

# 1. Clear remote dist
print("--- Clear remote dist ---")
run(f'rm -rf {remote_dist}', 3)

# 2. Upload all files
print("--- Uploading frontend dist ---")
uploaded = 0
skipped = 0
for root, dirs, files in os.walk(local_dist):
    for fname in files:
        local_path = os.path.join(root, fname)
        rel_path = os.path.relpath(local_path, local_dist)
        remote_path = f'{remote_dist}/{rel_path}'.replace('\\', '/')
        remote_dir = '/'.join(remote_path.rsplit('/', 1)[:-1])
        
        # Create remote dir
        parts = remote_dir.split('/')
        for i in range(1, len(parts)+1):
            d = '/'.join(parts[:i])
            try:
                sftp.stat(d)
            except:
                try:
                    sftp.mkdir(d)
                except:
                    pass
        
        # Upload file
        try:
            sftp.put(local_path, remote_path)
            uploaded += 1
            if uploaded % 5 == 0:
                print(f"  Uploaded {uploaded} files...")
        except Exception as e:
            skipped += 1
            print(f"  Skip {rel_path}: {e}")

print(f"Uploaded {uploaded} files, skipped {skipped}")

# 3. Verify
print("\n--- Verify ---")
result = run(f'ls {remote_dist}/', 3)
print(result[:300])

# 4. Check root
print("\n--- Root HTTP ---")
code = run('curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000/', 5)
print("HTTP:", code)
html = run('curl -s --max-time 5 http://127.0.0.1:3000/', 8)
print("HTML snippet:", html[:300])

sftp.close()
client.close()
print("\n=== DONE ===")
