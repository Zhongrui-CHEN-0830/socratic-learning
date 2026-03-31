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

# 1. Verify current index.html has CN mirrors
print('=== 1. Current index.html ===')
print(cmd('cat /opt/socratic-learning/frontend/dist/index.html', 3))

# 2. Test fonts.loli.net reachability from VPS
print('\n=== 2. fonts.loli.net reachable? ===')
print(cmd('curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 "https://fonts.loli.net/css2?family=Noto+Sans+SC" 2>&1', 8))

# 3. Test npmmirror reachable from VPS
print('\n=== 3. npmmirror reachable? ===')
print(cmd('curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 "https://registry.npmmirror.com/katex/0.16.9/files/dist/katex.min.css" 2>&1', 8))

# 4. Check PM2 error log for any JS runtime errors
print('\n=== 4. PM2 error log (last 30) ===')
print(cmd('tail -30 /root/.pm2/logs/socratic-learning-error.log 2>&1', 3))

# 5. Check if there's a console error in the JS bundle (look for obvious issues)
print('\n=== 5. Check JS bundle for obvious errors ===')
print(cmd('head -c 200 /opt/socratic-learning/frontend/dist/assets/index-BCly1JMD.js', 3))

# 6. Check if the app has a router issue (React Router)
print('\n=== 6. Check App.tsx routes ===')
print(cmd('cat /opt/socratic-learning/frontend/src/App.tsx 2>&1 | head -60', 3))

# 7. Check if there's a vite.config issue with base path
print('\n=== 7. vite.config.ts ===')
print(cmd('cat /opt/socratic-learning/frontend/vite.config.ts', 3))

# 8. Check if the CSS file loads correctly
print('\n=== 8. CSS file first 100 chars ===')
print(cmd('head -c 100 /opt/socratic-learning/frontend/dist/assets/index-CmltbenI.css', 3))

# 9. Simulate what browser does: fetch index.html then assets
print('\n=== 9. Full page load simulation ===')
print(cmd('curl -s http://127.0.0.1:80/ | grep -o "src=\"[^\"]*\"\|href=\"[^\"]*\"" | head -20', 3))

client.close()
print('\nDONE')
