import { Router } from 'express'
import { getSupabase } from '../lib/supabase.js'
import { authMiddleware, AuthRequest } from '../middleware/auth.js'

const router = Router()
router.use(authMiddleware)

router.get('/', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabase()
    const { data, error } = await supabase
      .from('diaries')
      .select('*')
      .eq('user_id', req.userId!)
      .order('date', { ascending: false })

    if (error) throw error
    res.json({ diaries: data || [] })
  } catch (err: unknown) {
    res.status(500).json({ error: 'Failed to load diaries' })
  }
})

export default router
