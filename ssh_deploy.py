import paramiko
import time
import base64
import io

host = '23.27.48.187'
port = 22
username = 'root'
password = 'wbBfRca7GcJdw6ueD0e5'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=username, password=password, timeout=10)
print("SSH connected!")

# Use invoke_shell for sudo commands that need password
def run_cmd(cmd, wait=5):
    stdin, stdout, stderr = client.exec_command(cmd)
    time.sleep(wait)
    out = stdout.read().decode('utf-8', errors='ignore')
    err = stderr.read().decode('utf-8', errors='ignore')
    return out + err

# Write file via SFTP (bypasses sudo password issue)
def write_file_sudo(remote_path, content):
    import io
    # Write directly via SFTP (connected as root)
    sftp = client.open_sftp()
    bio = io.BytesIO(content.encode('utf-8'))
    sftp.putfo(bio, remote_path)
    sftp.chmod(remote_path, 0o600)
    sftp.close()
    print(f"Written via SFTP: {remote_path}")

# 1. Install PM2
print("\n--- Installing PM2 ---")
result = run_cmd('npm install -g pm2', wait=20)
print(result[-300:])

# 2. Create .env
print("\n--- Creating .env ---")
env_content = """PORT=3000
NODE_ENV=production
SUPABASE_URL=https://uxtmvcextmbxdfwolpek.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NDc4MDg3MywiZXhwIjoyMDkwMzU2ODczfQ.uszQ9pLv1amc3972R_rhGql7z8hcmfby-dPT3dFHP3g
JWT_SECRET=069d7c72fb2d3d5e8a2f19c97359212b118174ef46dd577da91bcce91dcd8d5e
ENCRYPTION_KEY=117b8fe2d95162d8871982995e399a00b43d08738f3620592f5e1586692ac3a2
"""
write_file_sudo('/opt/socratic-learning/server/.env', env_content)
print(run_cmd('head -3 /opt/socratic-learning/server/.env', wait=3))

# 3. Install server dependencies
print("\n--- Installing server dependencies ---")
result = run_cmd('cd /opt/socratic-learning/server && npm install', wait=30)
print("npm install done, last 200 chars:", result[-200:])

# 4. Compile TypeScript
print("\n--- Compiling TypeScript ---")
result = run_cmd('cd /opt/socratic-learning/server && npx tsc', wait=30)
print("tsc result:", result[-300:])

# 5. Build frontend
print("\n--- Building frontend ---")
result = run_cmd('cd /opt/socratic-learning/frontend && npm install', wait=30)
print("frontend install:", result[-200:])
result = run_cmd('cd /opt/socratic-learning/frontend && npm run build', wait=60)
print("frontend build:", result[-300:])

# 6. PM2
print("\n--- PM2 setup ---")
run_cmd('pm2 delete socratic-learning 2>/dev/null; true', wait=3)
result = run_cmd('cd /opt/socratic-learning/server && pm2 start dist/index.js --name socratic-learning', wait=10)
print("pm2 start:", result[-200:])
run_cmd('pm2 save', wait=3)

# 7. Nginx config
print("\n--- Configuring Nginx ---")
nginx_content = """server {
    listen 80;
    server_name 23.27.48.187;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
"""
write_file_sudo('/etc/nginx/sites-available/default', nginx_content)
result = run_cmd('nginx -t', wait=3)
print("nginx -t:", result)
result = run_cmd('systemctl reload nginx', wait=5)
print("nginx reload:", result[-200:])

# 8. Firewall
print("\n--- Firewall ---")
for port in ['3000', '80', '443']:
    result = run_cmd(f'ufw allow {port}/tcp', wait=3)
    print(f"ufw {port}:", result[-100:])

# 9. PM2 startup
print("\n--- PM2 startup ---")
result = run_cmd('pm2 startup 2>&1 || true', wait=5)
print("pm2 startup:", result[-300:])
run_cmd('pm2 save', wait=3)

# Final check
print("\n--- Final Check ---")
result = run_cmd('pm2 list', wait=3)
print("pm2 list:", result)
result = run_cmd('curl -s http://localhost:3000/api/health', wait=5)
print("health check:", result)
result = run_cmd('curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/', wait=5)
print("http status:", result)

client.close()
print("\n=== ALL DONE ===")
