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

# Direct test: fetch JS via nginx port 80
print('=== 1. Fetch JS via nginx (port 80) ===')
print(cmd('curl -s -o /dev/null -w "%{http_code} content-type:%{content_type}" http://127.0.0.1:80/assets/index-BCly1JMD.js', 5))

# Direct test: fetch CSS via nginx
print('\n=== 2. Fetch CSS via nginx ===')
print(cmd('curl -s -o /dev/null -w "%{http_code} content-type:%{content_type}" http://127.0.0.1:80/assets/index-CmltbenI.css', 5))

# Direct test: fetch index.html via nginx
print('\n=== 3. Fetch / via nginx ===')
print(cmd('curl -s -o /dev/null -w "%{http_code} content-type:%{content_type}" http://127.0.0.1:80/', 5))

# Check nginx config
print('\n=== 4. Nginx config ===')
print(cmd('cat /etc/nginx/sites-enabled/default 2>&1 || cat /etc/nginx/sites-enabled/* 2>&1 || cat /etc/nginx/nginx.conf 2>&1 | head -60', 3))

# Check if there's a Google Fonts issue (index.html loads fonts from googleapis.com)
print('\n=== 5. Check index.html for external resources ===')
print(cmd('cat /opt/socratic-learning/frontend/dist/index.html', 3))

# Check if the JS file actually loads in browser (simulate with curl + follow redirects)
print('\n=== 6. Fetch JS via nginx with verbose ===')
print(cmd('curl -v -o /dev/null http://127.0.0.1:80/assets/index-BCly1JMD.js 2>&1 | head -20', 5))

# Check if there's a CSP or other header issue
print('\n=== 7. Full headers for JS asset ===')
print(cmd('curl -I http://127.0.0.1:80/assets/index-BCly1JMD.js 2>&1', 5))

client.close()
print('\nDONE')
