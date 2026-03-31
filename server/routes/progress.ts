import { Router } from 'express'
import { getSupabaseAdmin } from '../lib/supabase.js'
import { authMiddleware, AuthRequest } from '../middleware/auth.js'

const router = Router()
router.use(authMiddleware)

router.get('/', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabaseAdmin()
    const { textbook_id } = req.query
    let query = supabase
      .from('progress')
      .select('*')
      .eq('user_id', req.userId!)

    if (textbook_id) {
      query = query.eq('textbook_id', textbook_id)
    }

    const { data, error } = await query.order('created_at', { ascending: false })
    if (error) throw error
    res.json({ progress: data || [] })
  } catch (err: unknown) {
    res.status(500).json({ error: 'Failed to load progress' })
  }
})

export default router
