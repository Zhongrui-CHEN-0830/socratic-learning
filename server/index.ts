import 'dotenv/config'
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
