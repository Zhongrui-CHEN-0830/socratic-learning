import { Router } from 'express'
import multer from 'multer'
import path from 'path'
import { getSupabaseAdmin } from '../lib/supabase.js'
import { authMiddleware, AuthRequest } from '../middleware/auth.js'

const router = Router()
router.use(authMiddleware)

// Multer: store in memory, we'll upload to Supabase Storage
const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: 10 * 1024 * 1024 }, // 10MB
  fileFilter: (_req, file, cb) => {
    if (!file.originalname.endsWith('.md')) {
      cb(new Error('Only .md files are allowed'))
      return
    }
    cb(null, true)
  },
})

// List textbooks
router.get('/', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabaseAdmin()
    const { data, error } = await supabase
      .from('textbooks')
      .select('*')
      .eq('user_id', req.userId!)
      .order('created_at', { ascending: false })

    if (error) throw error
    res.json({ textbooks: data || [] })
  } catch (err: unknown) {
    console.error('List textbooks error:', err)
    res.status(500).json({ error: 'Failed to list textbooks' })
  }
})

// Upload textbook
router.post('/upload', upload.single('textbook'), async (req: AuthRequest, res) => {
  try {
    if (!req.file) {
      res.status(400).json({ error: 'No file uploaded' })
      return
    }

    const supabase = getSupabaseAdmin()
    const filename = req.file.originalname
    const storagePath = `${req.userId}/${Date.now()}-${filename}`

    // Upload to Supabase Storage
    const { error: uploadError } = await supabase.storage
      .from('textbooks')
      .upload(storagePath, req.file.buffer, {
        contentType: 'text/markdown',
        upsert: false,
      })

    if (uploadError) throw uploadError

    // Store metadata in DB
    const { data, error } = await supabase
      .from('textbooks')
      .insert({
        user_id: req.userId!,
        filename,
        storage_path: storagePath,
        file_size: req.file.size,
      })
      .select()
      .single()

    if (error) throw error
    res.json({ textbook: data })
  } catch (err: unknown) {
    console.error('Upload textbook error:', err)
    res.status(500).json({ error: 'Failed to upload textbook' })
  }
})

// Download / read textbook content
router.get('/:id/content', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabaseAdmin()
    const { data, error } = await supabase
      .from('textbooks')
      .select('storage_path')
      .eq('id', req.params.id)
      .eq('user_id', req.userId!)
      .maybeSingle()

    if (error || !data) {
      res.status(404).json({ error: 'Textbook not found' })
      return
    }

    const { data: fileData, error: fileError } = await supabase.storage
      .from('textbooks')
      .download(data.storage_path)

    if (fileError || !fileData) {
      res.status(404).json({ error: 'File not found in storage' })
      return
    }

    const content = await fileData.text()
    res.json({ content })
  } catch (err: unknown) {
    console.error('Get textbook content error:', err)
    res.status(500).json({ error: 'Failed to get textbook' })
  }
})

// Delete textbook
router.delete('/:id', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabaseAdmin()

    // Get storage path first
    const { data } = await supabase
      .from('textbooks')
      .select('storage_path')
      .eq('id', req.params.id)
      .eq('user_id', req.userId!)
      .maybeSingle()

    if (data?.storage_path) {
      await supabase.storage
        .from('textbooks')
        .remove([data.storage_path])
    }

    await supabase
      .from('textbooks')
      .delete()
      .eq('id', req.params.id)
      .eq('user_id', req.userId!)

    res.json({ ok: true })
  } catch (err: unknown) {
    res.status(500).json({ error: 'Failed to delete textbook' })
  }
})

export default router
