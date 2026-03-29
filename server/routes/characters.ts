import { Router } from 'express'
import { getSupabase } from '../lib/supabase.js'
import { authMiddleware, AuthRequest } from '../middleware/auth.js'

const router = Router()
router.use(authMiddleware)

// Get character states for current user
router.get('/state', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabase()
    const { data, error } = await supabase
      .from('character_states')
      .select('*')
      .eq('user_id', req.userId!)

    if (error) throw error
    res.json({ states: data || [] })
  } catch (err: unknown) {
    res.status(500).json({ error: 'Failed to get character states' })
  }
})

// Get character log history
router.get('/logs', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabase()
    const { data, error } = await supabase
      .from('character_states')
      .select('character_id, log, updated_at')
      .eq('user_id', req.userId!)

    if (error) throw error
    res.json({ logs: data || [] })
  } catch (err: unknown) {
    res.status(500).json({ error: 'Failed to get character logs' })
  }
})

export default router
