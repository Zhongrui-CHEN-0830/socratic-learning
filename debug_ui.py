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

# 1. PM2 status
print('=== 1. PM2 status ===')
print(cmd('pm2 list 2>&1', 4))

# 2. Health check
print('=== 2. Health check ===')
print(cmd('curl -s http://127.0.0.1:3000/api/health', 5))

# 3. Nginx status
print('=== 3. Nginx status ===')
print(cmd('systemctl status nginx 2>&1 | head -20', 4))

# 4. Does index.html exist?
print('=== 4. Frontend dist index.html ===')
print(cmd('ls -la /opt/socratic-learning/frontend/dist/ 2>&1', 3))

# 5. Try fetching the page via curl
print('=== 5. Fetch / via nginx ===')
print(cmd('curl -s -o /dev/null -w "%{http_code} %{size_download}bytes" http://127.0.0.1:80/', 5))

# 6. Fetch the actual HTML
print('\n=== 6. HTML content (first 500 chars) ===')
print(cmd('curl -s http://127.0.0.1:80/ | head -c 500', 5))

# 7. Check JS/CSS assets
print('\n=== 7. Assets in dist ===')
print(cmd('ls -la /opt/socratic-learning/frontend/dist/assets/', 3))

# 8. Try fetching a JS asset
print('\n=== 8. Fetch JS asset (first 100 chars) ===')
print(cmd('ls /opt/socratic-learning/frontend/dist/assets/*.js | head -1 | xargs -I{} curl -s http://127.0.0.1:80/assets/$(basename {}) | head -c 100', 5))

# 9. PM2 error log (last 20 lines)
print('\n=== 9. PM2 error log (last 20) ===')
print(cmd('tail -20 /root/.pm2/logs/socratic-learning-error.log 2>&1', 3))

# 10. PM2 out log (last 10 lines)
print('\n=== 10. PM2 out log (last 10) ===')
print(cmd('tail -10 /root/.pm2/logs/socratic-learning-out.log 2>&1', 3))

# 11. Nginx error log
print('\n=== 11. Nginx error log (last 10) ===')
print(cmd('tail -10 /var/log/nginx/error.log 2>&1', 3))

# 12. Check if server is actually serving static files
print('\n=== 12. STATIC_DIR env check ===')
print(cmd('grep STATIC_DIR /opt/socratic-learning/server/.env', 3))
print(cmd('ls -la /opt/socratic-learning/frontend/dist/index.html 2>&1', 3))

client.close()
print('\nDONE')
