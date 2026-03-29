import paramiko, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=10, auth_timeout=10)
client.get_transport().set_keepalive(5)
print("SSH connected!")

def run(cmd, wait=8):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=20)
    time.sleep(wait)
    return (stdout.read() + stderr.read()).decode('utf-8', errors='replace')

# 1. Kill existing pm2
print("\n--- Kill existing PM2 ---")
print(run('pm2 delete socratic-learning 2>/dev/null; true', 3))

# 2. Pull latest
print("\n--- Git pull ---")
print(run('cd /opt/socratic-learning && git pull origin main', 10)[:400])

# 3. Install tsx
print("\n--- Install tsx ---")
print(run('cd /opt/socratic-learning/server && npm install tsx', 20)[:200])

# 4. Write .env
import io
env_content = """PORT=3000
NODE_ENV=production
SUPABASE_URL=https://uxtmvcextmbxdfwolpek.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NDc4MDg3MywiZXhwIjoyMDkwMzU2ODczfQ.uszQ9pLv1amc3972R_rhGql7z8hcmfby-dPT3dFHP3g
JWT_SECRET=069d7c72fb2d3d5e8a2f19c97359212b118174ef46dd577da91bcce91dcd8d5e
ENCRYPTION_KEY=117b8fe2d95162d8871982995e399a00b43d08738f3620592f5e1586692ac3a2
"""
sftp = client.open_sftp()
bio = io.BytesIO(env_content.encode('utf-8'))
sftp.putfo(bio, '/opt/socratic-learning/server/.env')
sftp.chmod('/opt/socratic-learning/server/.env', 0o600)
sftp.close()
print("Written .env")

# 5. Start with tsx (no compilation needed)
print("\n--- Start with tsx ---")
# Use pm2 start with tsx interpreter
start_script = 'cd /opt/socratic-learning/server && pm2 start npx --name socratic-learning -- tsx index.ts'
print(run(start_script, 10)[:300])

# 6. Wait for startup
print("\n--- Wait 8s ---")
time.sleep(8)

# 7. Health check
print("\n--- Health check ---")
result = run('curl -s --max-time 5 http://127.0.0.1:3000/api/health', 8)
print("health:", result)

# 8. HTTP status
print("\n--- HTTP status ---")
print(run('curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000/', 5))

# 9. Nginx config
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
bio2 = io.BytesIO(nginx_content.encode('utf-8'))
sftp2 = client.open_sftp()
sftp2.putfo(bio2, '/etc/nginx/sites-available/default')
sftp2.close()
print("Nginx written")
print(run('nginx -t && systemctl reload nginx', 5)[:200])

# 10. Firewall
print("\n--- Firewall ---")
for p in ['3000', '80', '443']:
    print(run(f'ufw allow {p}/tcp 2>/dev/null || true', 3)[:80])

# 11. Save PM2
print("\n--- PM2 save ---")
print(run('pm2 save', 3))
print(run('pm2 startup 2>&1 || true', 5)[:200])

# 12. Final logs
print("\n--- PM2 logs ---")
print(run('pm2 logs --lines 15 --nostream 2>&1', 5))

client.close()
print("\n=== ALL DONE ===")
