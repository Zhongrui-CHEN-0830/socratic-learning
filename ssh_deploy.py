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

# Step 1: Git force pull
print("1. Git force pull...")
print(cmd('cd /opt/socratic-learning && git fetch origin main && git reset --hard origin/main', 10)[:300])

# Step 2: Write fixed index.ts with express.json() on auth route
index_ts = """import 'dotenv/config'
import express from 'express'
import cors from 'cors'
import path from 'path'
import { fileURLToPath } from 'url'

import authRoutes from './routes/auth.js'
import userRoutes from './routes/user.js'
import textbookRoutes from './routes/textbooks.js'
import conversationRoutes from './routes/conversations.js'
import chatRoutes from './routes/chat.js'
import characterRoutes from './routes/characters.js'
import diaryRoutes from './routes/diaries.js'
import progressRoutes from './routes/progress.js'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const app = express()
const PORT = process.env.PORT || 3000

app.use(cors())

const distPath = process.env.STATIC_DIR || path.join(__dirname, '..', '..', 'frontend', 'dist')
app.use(express.static(distPath))

app.get('/api/health', (_req, res) => {
  res.json({ status: 'ok', time: new Date().toISOString() })
})

// Auth: JSON body needed for login/register
app.use('/api/auth', express.json({ limit: '2mb' }), authRoutes)

// User: needs JSON body
app.use('/api/user', express.json({ limit: '2mb' }), userRoutes)

// Textbooks: uses multer for multipart - NO express.json()
app.use('/api/textbooks', textbookRoutes)

// Conversations: needs JSON body
app.use('/api/conversations', express.json({ limit: '2mb' }), conversationRoutes)

// Chat: needs JSON body
app.use('/api/chat', express.json({ limit: '2mb' }), chatRoutes)

// Characters: needs JSON body
app.use('/api/characters', express.json({ limit: '2mb' }), characterRoutes)

// Diaries: needs JSON body
app.use('/api/diaries', express.json({ limit: '2mb' }), diaryRoutes)

// Progress: needs JSON body
app.use('/api/progress', express.json({ limit: '2mb' }), progressRoutes)

// Serve frontend for all non-API routes (SPA)
app.get('*', (_req, res) => {
  res.sendFile(path.join(distPath, 'index.html'), (err) => {
    if (err) {
      res.status(200).send('<html><body style="background:#1a1612;color:#c9a84c;font-family:serif;text-align:center;padding:80px"><h1>墨韵书院</h1><p>服务器已启动，正在等待前端构建...</p></body></html>')
    }
  })
})

app.listen(PORT, () => {
  console.log('墨韵书院服务器已启动')
  console.log('本地访问: http://localhost:' + PORT)
})
"""

bio = io.BytesIO(index_ts.encode('utf-8'))
sftp = client.open_sftp()
sftp.putfo(bio, '/opt/socratic-learning/server/index.ts')
sftp.close()
print("index.ts written via SFTP")

# Step 3: Write fixed auth.ts
auth_ts = """import { Router } from 'express'
import { getSupabaseAdmin, getSupabase } from '../lib/supabase.js'
import { generateToken, authMiddleware } from '../middleware/auth.js'

const router = Router()

router.post('/register', async (req: any, res: any) => {
  try {
    const { email, password } = req.body
    if (!email || !password) { res.status(400).json({ error: 'Email and password required' }); return }
    if (password.length < 8) { res.status(400).json({ error: 'Password must be 8+ chars' }); return }
    const supabase = getSupabaseAdmin()
    const { data: authData, error: authError } = await supabase.auth.admin.createUser({ email, password, email_confirm: true })
    if (authError || !authData.user) { res.status(409).json({ error: authError?.message || 'Registration failed' }); return }
    const userId = authData.user.id
    await supabase.from('profiles').insert({ id: userId, email, nickname: email.split('@')[0] })
    await supabase.from('character_states').insert([
      { user_id: userId, character_id: 'mu', affection: 50, strictness: 50, mood: {}, log: [] },
      { user_id: userId, character_id: 'sang', affection: 50, strictness: 50, mood: {}, log: [] },
    ])
    const token = generateToken(userId, email)
    res.json({ token, user: { id: userId, email } })
  } catch (err) { console.error('Register error:', err); res.status(500).json({ error: 'Server error' }) }
})

router.post('/login', async (req: any, res: any) => {
  try {
    const { email, password } = req.body
    if (!email || !password) { res.status(400).json({ error: 'Email and password required' }); return }
    const supabase = getSupabase()
    const { data, error } = await supabase.auth.signInWithPassword({ email, password })
    if (error || !data.user) { res.status(401).json({ error: 'Email or password incorrect' }); return }
    const token = generateToken(data.user.id, data.user.email!)
    res.json({ token, user: { id: data.user.id, email: data.user.email } })
  } catch (err) { console.error('Login error:', err); res.status(500).json({ error: 'Server error' }) }
})

router.get('/me', authMiddleware, async (req: any, res: any) => {
  const userId = (req as any).userId
  if (!userId) { res.status(401).json({ error: 'Unauthorized' }); return }
  const supabase = getSupabaseAdmin()
  const { data: profile } = await supabase.from('profiles').select('*').eq('id', userId).maybeSingle()
  res.json({ user: profile ? { id: profile.id, email: profile.email, nickname: profile.nickname } : null })
})

export default router
"""

bio2 = io.BytesIO(auth_ts.encode('utf-8'))
sftp2 = client.open_sftp()
sftp2.putfo(bio2, '/opt/socratic-learning/server/routes/auth.ts')
sftp2.close()
print("auth.ts written via SFTP")

# Step 4: Clean rebuild
print("\n2. Clean rebuild TypeScript...")
result = cmd('cd /opt/socratic-learning/server && rm -rf dist && npx tsc 2>&1', 30)
if 'error' in result.lower() and 'error TS' in result:
    print("TSC ERRORS:", result[:500])
else:
    print("TSC: compiled OK" if result.strip() == '' else result[:300])

# Verify compiled index.js has express.json for auth
print("\n3. Verify compiled index.js has express.json for /api/auth:")
verify = cmd('grep -A1 "/api/auth" /opt/socratic-learning/server/dist/index.js', 3)
print(verify[:200])

# Step 5: PM2 restart
print("\n4. Restart PM2...")
print(cmd('pm2 restart socratic-learning', 8)[:200])

time.sleep(8)

print("\n5. Health:", cmd('curl -s http://127.0.0.1:3000/api/health', 5))

print("\n6. Test register:")
print(cmd('curl -s -X POST http://127.0.0.1:3000/api/auth/register -H "Content-Type: application/json" -d \'{"email":"apitest@example.com","password":"testpass123"}\'', 10)[:400])

print("\n7. PM2 errors (last 3):")
print(cmd('tail -3 /root/.pm2/logs/socratic-learning-error.log 2>&1', 5)[:300])

client.close()
print("\nDONE")
