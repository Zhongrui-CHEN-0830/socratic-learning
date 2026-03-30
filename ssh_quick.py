import paramiko, time, sys, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
host, port, user, pw = '23.27.48.187', 22, 'root', 'wbBfRca7GcJdw6ueD0e5'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=pw, timeout=15)
client.get_transport().set_keepalive(5)
print("connected")

env_content = """PORT=3000
NODE_ENV=production
STATIC_DIR=/opt/socratic-learning/frontend/dist
SUPABASE_URL=https://uxtmvcextmbxdfwolpek.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3ODA4NzMsImV4cCI6MjA5MDM1Njg3M30.Fqt90hnm8PLaeb287XU_StOuSob68HMcylJKOmkfEio
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4dG12Y2V4dG1ieGRmd29scGVrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NDc4MDg3MywiZXhwIjoyMDkwMzU2ODczfQ.uszQ9pLv1amc3972R_rhGql7z8hcmfby-dPT3dFHP3g
JWT_SECRET=069d7c72fb2d3d5e8a2f19c97359212b118174ef46dd577da91bcce91dcd8d5e
ENCRYPTION_KEY=117b8fe2d95162d8871982995e399a00b43d08738f3620592f5e1586692ac3a2
"""

bio = io.BytesIO(env_content.encode('utf-8'))
sftp = client.open_sftp()
sftp.putfo(bio, '/opt/socratic-learning/server/.env')
sftp.chmod('/opt/socratic-learning/server/.env', 0o600)
sftp.close()
print("Written .env")

# Fix index.ts: express.json() must be AFTER file upload routes
# Read current index.ts
chan = client.get_transport().open_session()
chan.exec_command('cat /opt/socratic-learning/server/index.ts')
time.sleep(3)
content = chan.recv(16384).decode('utf-8', errors='replace')
chan.close()
print("Current index.ts content length:", len(content))

# Write fixed index.ts
fixed_index = """import 'dotenv/config'
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

// CORS first
app.use(cors())

// IMPORTANT: express.json() must be AFTER textbook upload routes
// so that multipart form-data is NOT parsed as JSON
app.use('/api/textbooks', express.json({ limit: '2mb' }))

// Serve built frontend in production
const distPath = process.env.STATIC_DIR || path.join(__dirname, '..', '..', 'frontend', 'dist')
app.use(express.static(distPath))

// API Routes (no global express.json() at top)
// Auth routes (no JSON body needed for GET)
app.use('/api/auth', authRoutes)

// JSON parser for routes that need it
app.use(express.json({ limit: '2mb' }))

// Other routes
app.use('/api/user', userRoutes)
app.use('/api/textbooks', textbookRoutes)
app.use('/api/conversations', conversationRoutes)
app.use('/api/chat', chatRoutes)
app.use('/api/characters', characterRoutes)
app.use('/api/diaries', diaryRoutes)
app.use('/api/progress', progressRoutes)

// Health check
app.get('/api/health', (_req, res) => {
  res.json({ status: 'ok', time: new Date().toISOString() })
})

// Serve frontend for all non-API routes (SPA)
app.get('*', (_req, res) => {
  res.sendFile(path.join(distPath, 'index.html'), (err) => {
    if (err) {
      res.status(200).send('<html><body style="background:#1a1612;color:#c9a84c;font-family:serif;text-align:center;padding:80px"><h1>墨韵书院</h1><p>服务器启动中...</p></body></html>')
    }
  })
})

app.listen(PORT, () => {
  console.log('\\n  墨韵书院服务器已启动')
  console.log('  本地访问: http://localhost:' + PORT)
  console.log('  生产模式: 前端静态文件已配置\\n')
})
"""

bio2 = io.BytesIO(fixed_index.encode('utf-8'))
sftp2 = client.open_sftp()
sftp2.putfo(bio2, '/opt/socratic-learning/server/index.ts')
sftp2.close()
print("Written fixed index.ts")

# Restart PM2
def cmd(c, wait=8):
    chan = client.get_transport().open_session()
    chan.exec_command(c)
    time.sleep(wait)
    return chan.recv(16384).decode('utf-8', errors='replace')

print("\nRestarting PM2...")
print(cmd('pm2 restart socratic-learning', 8)[:200])
time.sleep(8)
print("\nHealth:", cmd('curl -s http://127.0.0.1:3000/api/health', 5))

client.close()
print("\nDONE")
