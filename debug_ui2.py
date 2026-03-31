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

# 1. What does Express actually serve for /assets/index-BCly1JMD.js?
print('=== 1. Direct Express (port 3000) for JS asset ===')
print(cmd('curl -s -o /dev/null -w "%{http_code} content-type:%{content_type}" http://127.0.0.1:3000/assets/index-BCly1JMD.js', 5))

# 2. Check the actual file path
print('\n=== 2. Actual file path ===')
print(cmd('ls -la /opt/socratic-learning/frontend/dist/assets/index-BCly1JMD.js', 3))

# 3. Check what STATIC_DIR resolves to in the running process
print('\n=== 3. Check compiled index.js distPath ===')
print(cmd('grep -n "distPath\|STATIC_DIR\|static" /opt/socratic-learning/server/dist/index.js | head -10', 3))

# 4. Check what __dirname is in the compiled dist
print('\n=== 4. Where is dist/index.js? ===')
print(cmd('ls -la /opt/socratic-learning/server/dist/index.js', 3))

# 5. Compute what distPath would be
# __dirname = /opt/socratic-learning/server/dist
# path.join(__dirname, '..', '..', 'frontend', 'dist')
# = /opt/socratic-learning/server/dist/../../frontend/dist
# = /opt/socratic-learning/frontend/dist  ← should be correct
print('\n=== 5. Verify computed path ===')
print(cmd('ls -la /opt/socratic-learning/server/dist/../../frontend/dist/', 3))

# 6. But STATIC_DIR is set, so it uses that
print('\n=== 6. STATIC_DIR value ===')
print(cmd('grep STATIC_DIR /opt/socratic-learning/server/.env', 3))
print(cmd('ls -la /opt/socratic-learning/frontend/dist/', 3))

# 7. Try fetching JS directly from Express
print('\n=== 7. Fetch JS from Express directly (verbose) ===')
print(cmd('curl -v http://127.0.0.1:3000/assets/index-BCly1JMD.js 2>&1 | head -30', 5))

# 8. Check if the file is actually readable
print('\n=== 8. File readable? ===')
print(cmd('head -c 50 /opt/socratic-learning/frontend/dist/assets/index-BCly1JMD.js', 3))

client.close()
print('\nDONE')
