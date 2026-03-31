"""
Socratic Learning 部署脚本
自动处理：前端 .env 创建 → Git 拉取 → 服务端构建 → 前端构建 → PM2 重启
"""
import paramiko, time, sys, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HOST, PORT = '23.27.48.187', 22
USER, PW   = 'root', 'wbBfRca7GcJdw6ueD0e5'

def cmd(ssh, c, wait=8):
    chan = ssh.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    out = chan.recv(65536).decode('utf-8', errors='replace')
    err = chan.recv_stderr(16384).decode('utf-8', errors='replace')
    return out + err

def deploy():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOST, port=PORT, username=USER, password=PW, timeout=15)

    # Step 1: Read server .env for Supabase credentials
    print('=== 1. 读取服务端 .env ===')
    env_text = cmd(ssh, 'cat /opt/socratic-learning/server/.env', 4)
    supabase_url = ''
    supabase_anon_key = ''
    for line in env_text.splitlines():
        if line.startswith('SUPABASE_URL='):
            supabase_url = line.split('=', 1)[1].strip()
        elif line.startswith('SUPABASE_ANON_KEY='):
            supabase_anon_key = line.split('=', 1)[1].strip()

    if not supabase_url or not supabase_anon_key:
        print('ERROR: 无法读取 Supabase 配置')
        return

    print(f'  SUPABASE_URL: {supabase_url}')
    print(f'  ANON_KEY: {supabase_anon_key[:30]}...')

    # Step 2: Create frontend/.env
    print('\n=== 2. 创建 frontend/.env ===')
    frontend_env = f'VITE_SUPABASE_URL={supabase_url}\nVITE_SUPABASE_ANON_KEY={supabase_anon_key}\n'
    sftp = ssh.open_sftp()
    f = sftp.open('/opt/socratic-learning/frontend/.env', 'w')
    f.write(frontend_env)
    f.close()
    sftp.close()
    print('  frontend/.env 已写入')

    # Step 3: Git pull
    print('\n=== 3. Git pull ===')
    print(cmd(ssh, 'cd /opt/socratic-learning && git pull origin main 2>&1', 10)[:400])

    # Step 4: Rebuild server
    print('\n=== 4. 重建服务端 ===')
    r = cmd(ssh, 'cd /opt/socratic-learning/server && rm -rf dist && npx tsc 2>&1', 30)
    if 'error TS' in r:
        print('  TSC 错误:', r[:500])
    else:
        print('  TSC 编译成功')

    # Step 5: Rebuild frontend (now with .env)
    print('\n=== 5. 重建前端 ===')
    r2 = cmd(ssh, 'cd /opt/socratic-learning/frontend && npm run build 2>&1', 60)
    print(r2[-400:] if len(r2) > 400 else r2)

    # Step 6: Verify supabase URL in bundle
    print('\n=== 6. 验证 bundle ===')
    verify = cmd(ssh, "grep -c 'uxtmvcextmbxdfwolpek' /opt/socratic-learning/frontend/dist/assets/index-*.js 2>&1", 3).strip()
    print(f'  Supabase URL in bundle: {"✓ 已包含" if verify == "1" else "✗ 未找到 (" + verify + ")"}')

    # Step 7: Restart PM2
    print('\n=== 7. 重启 PM2 ===')
    print(cmd(ssh, 'pm2 restart socratic-learning 2>&1', 6)[-200:])

    time.sleep(4)

    # Step 8: Health check
    print('\n=== 8. 健康检查 ===')
    health = cmd(ssh, 'curl -s http://127.0.0.1:3000/api/health', 5)
    print(f'  {health}')

    ssh.close()
    print('\n部署完成！')

if __name__ == '__main__':
    deploy()
