import paramiko, time, sys, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)
client.get_transport().set_keepalive(5)
print("connected")

def cmd(c, wait=8):
    chan = client.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    return chan.recv(16384).decode('utf-8', errors='replace')

# Fix auth.ts: add AuthRequest interface and use it
fix_auth = """import { Router } from 'express'
import { getSupabaseAdmin, getSupabase } from '../lib/supabase.js'
import { generateToken } from '../middleware/auth.js'

// Extend Express Request to include userId
declare global {
  namespace Express {
    interface Request {
      userId?: string
      userEmail?: string
    }
  }
}

const router = Router()

router.post('/register', async (req, res) => {
  try {
    const { email, password } = req.body
    if (!email || !password) {
      res.status(400).json({ error: 'Email and password are required' })
      return
    }
    if (password.length < 8) {
      res.status(400).json({ error: '密码至少需要 8 位' })
      return
    }

    const supabase = getSupabaseAdmin()

    // Create auth user
    const { data: authData, error: authError } = await supabase.auth.admin.createUser({
      email,
      password,
      email_confirm: true,
    })

    if (authError || !authData.user) {
      res.status(409).json({ error: authError?.message || '注册失败，邮箱可能已被使用' })
      return
    }

    const userId = authData.user.id

    // Create profile
    await supabase.from('profiles').insert({
      id: userId,
      email,
      nickname: email.split('@')[0],
    })

    // Initialize character states
    await supabase.from('character_states').insert([
      { user_id: userId, character_id: 'mu', affection: 50, strictness: 50, mood: {}, log: [] },
      { user_id: userId, character_id: 'sang', affection: 50, strictness: 50, mood: {}, log: [] },
    ])

    const token = generateToken(userId, email)
    res.json({ token, user: { id: userId, email } })
  } catch (err) {
    console.error('Register error:', err)
    res.status(500).json({ error: '服务器错误' })
  }
})

router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body
    if (!email || !password) {
      res.status(400).json({ error: 'Email and password are required' })
      return
    }

    // Use public Supabase client for auth
    const supabase = getSupabase()
    const { data: signInData, error: signInError } = await supabase.auth.signInWithPassword({
      email,
      password,
    })

    if (signInError || !signInData.user) {
      res.status(401).json({ error: '邮箱或密码错误' })
      return
    }

    const token = generateToken(signInData.user.id, signInData.user.email!)
    res.json({ token, user: { id: signInData.user.id, email: signInData.user.email } })
  } catch (err) {
    console.error('Login error:', err)
    res.status(500).json({ error: '服务器错误' })
  }
})

router.get('/me', async (req, res) => {
  const authReq = req as Express.Request & { userId?: string; userEmail?: string }
  if (!authReq.userId) {
    res.status(401).json({ error: 'Unauthorized' })
    return
  }

  const supabase = getSupabaseAdmin()
  const { data: profile } = await supabase
    .from('profiles')
    .select('*')
    .eq('id', authReq.userId)
    .maybeSingle()

  res.json({
    user: profile ? { id: profile.id, email: profile.email, nickname: profile.nickname } : null,
  })
})

export default router
"""

bio = io.BytesIO(fix_auth.encode('utf-8'))
sftp = client.open_sftp()
sftp.putfo(bio, '/opt/socratic-learning/server/routes/auth.ts')
sftp.close()
print("Written fixed auth.ts")

# Recompile
print("\nRecompile:")
print(cmd('cd /opt/socratic-learning/server && rm -rf dist && npx tsc 2>&1', 30)[:400])

# Restart
print("\nRestart PM2:")
print(cmd('pm2 restart socratic-learning', 8)[:200])
time.sleep(8)

print("\nHealth:", cmd('curl -s http://127.0.0.1:3000/api/health', 5))

client.close()
print("\nDONE")
