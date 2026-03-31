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

# 1. What does the CSS bundle actually start with now?
print('=== 1. CSS bundle first 300 chars ===')
print(cmd('head -c 300 /opt/socratic-learning/frontend/dist/assets/index-CmMo5lYR.css', 3))

# 2. Does the CSS bundle have ANY googleapis reference?
print('\n=== 2. googleapis in CSS bundle? ===')
print(cmd('grep -c "googleapis" /opt/socratic-learning/frontend/dist/assets/index-CmMo5lYR.css 2>&1', 3))

# 3. Does the CSS bundle have loli.net?
print('\n=== 3. loli.net in CSS bundle? ===')
print(cmd('grep -c "loli.net" /opt/socratic-learning/frontend/dist/assets/index-CmMo5lYR.css 2>&1', 3))

# 4. What does index.html look like now?
print('\n=== 4. Current index.html ===')
print(cmd('cat /opt/socratic-learning/frontend/dist/index.html', 3))

# 5. Full HTTP response for the page (headers + first 500 chars of body)
print('\n=== 5. Full HTTP response for / ===')
print(cmd('curl -v http://127.0.0.1:80/ 2>&1 | head -40', 5))

# 6. Check if fonts.loli.net is actually accessible from the VPS
print('\n=== 6. fonts.loli.net DNS + connect test ===')
print(cmd('curl -v --connect-timeout 5 "https://fonts.loli.net/css2?family=Noto+Sans+SC" 2>&1 | head -20', 8))

# 7. Check if npmmirror KaTeX CSS is accessible
print('\n=== 7. npmmirror KaTeX CSS test ===')
print(cmd('curl -s -o /dev/null -w "%{http_code} size:%{size_download}" --connect-timeout 5 "https://registry.npmmirror.com/katex/0.16.9/files/dist/katex.min.css" 2>&1', 8))

# 8. PM2 error log - any new errors?
print('\n=== 8. PM2 error log (last 15) ===')
print(cmd('tail -15 /root/.pm2/logs/socratic-learning-error.log 2>&1', 3))

# 9. Check if there's a JS error - look at the bundle for any obvious issues
print('\n=== 9. JS bundle - check for loli.net or googleapis ===')
print(cmd('grep -c "googleapis" /opt/socratic-learning/frontend/dist/assets/index-CEgTZ6r9.js 2>&1', 3))

# 10. What does the browser actually get? Simulate full page load
print('\n=== 10. Simulate browser: fetch page + check all linked resources ===')
print(cmd('curl -s http://127.0.0.1:80/ | grep -E "src=|href=" | head -10', 3))

client.close()
print('\nDONE')
