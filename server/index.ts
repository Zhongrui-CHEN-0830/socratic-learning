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

// Middleware
app.use(cors())
app.use(express.json({ limit: '2mb' }))

// Serve built frontend in production
const distPath = process.env.STATIC_DIR || path.join(__dirname, '..', '..', 'frontend', 'dist')
app.use(express.static(distPath))

// API Routes
app.use('/api/auth', authRoutes)
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
      // If dist doesn't exist yet, send a message
      res.status(200).send(`
        <html>
          <body style="background:#1a1612;color:#c9a84c;font-family:serif;text-align:center;padding:80px">
            <h1>墨韵书院</h1>
            <p>服务器已启动，正在等待前端构建...</p>
            <p style="color:#6a6258;font-size:14px">Run <code>cd frontend && npm run build</code> first</p>
          </body>
        </html>
      `)
    }
  })
})

app.listen(PORT, () => {
  console.log(`\n  墨韵书院服务器已启动`)
  console.log(`  本地访问: http://localhost:${PORT}`)
  console.log(`  生产模式: 前端静态文件已配置\n`)
})
