import paramiko
import time
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

host = '23.27.48.187'
port = 22
username = 'root'
password = 'wbBfRca7GcJdw6ueD0e5'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=username, password=password, timeout=10)
print("SSH connected!")

def run_cmd(cmd, wait=8):
    stdin, stdout, stderr = client.exec_command(cmd)
    time.sleep(wait)
    out = stdout.read().decode('utf-8', errors='replace')
    err = stderr.read().decode('utf-8', errors='replace')
    return out + err

# 1. Pull latest code
print("\n--- Pulling latest code ---")
result = run_cmd('cd /opt/socratic-learning && git pull origin main', wait=10)
print("git pull:", result[-300:])

# 2. Re-install server deps (in case new deps added)
print("\n--- Server npm install ---")
result = run_cmd('cd /opt/socratic-learning/server && npm install', wait=30)
print("npm install:", result[-300:])

# 3. Compile TypeScript
print("\n--- Compiling TypeScript ---")
result = run_cmd('cd /opt/socratic-learning/server && npx tsc', wait=30)
print("tsc:", result[-400:])

# 4. Build frontend
print("\n--- Building frontend ---")
result = run_cmd('cd /opt/socratic-learning/frontend && npm install', wait=30)
print("frontend install:", result[-200:])
result = run_cmd('cd /opt/socratic-learning/frontend && npm run build', wait=60)
print("frontend build:", result[-400:])

# 5. Restart PM2
print("\n--- Restarting PM2 ---")
run_cmd('pm2 delete socratic-learning 2>/dev/null; true', wait=3)
result = run_cmd('cd /opt/socratic-learning/server && pm2 start dist/index.js --name socratic-learning', wait=10)
print("pm2 start:", result[-200:])
run_cmd('pm2 save', wait=3)
run_cmd('pm2 startup 2>&1 || true', wait=5)

# 6. Configure Nginx
print("\n--- Nginx config ---")
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
import io
sftp = client.open_sftp()
bio = io.BytesIO(nginx_content.encode('utf-8'))
sftp.putfo(bio, '/etc/nginx/sites-available/default')
sftp.close()
print("Nginx config written")
result = run_cmd('nginx -t', wait=5)
print("nginx -t:", result)
result = run_cmd('systemctl reload nginx', wait=5)
print("nginx reload:", result[-200:])

# 7. Firewall
print("\n--- Firewall ---")
for p in ['3000', '80', '443']:
    result = run_cmd(f'ufw allow {p}/tcp', wait=3)
    print(f"ufw {p}:", result[-80:])

# Final check
print("\n--- Final Check ---")
result = run_cmd('pm2 list', wait=3)
print("pm2:", result)
result = run_cmd('curl -s http://localhost:3000/api/health', wait=5)
print("health:", result)
result = run_cmd('curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/', wait=5)
print("http status:", result)

client.close()
print("\n=== ALL DONE ===")
