import { Router } from 'express'
import { getSupabase } from '../lib/supabase.js'
import { authMiddleware, AuthRequest } from '../middleware/auth.js'

const router = Router()
router.use(authMiddleware)

// List conversations
router.get('/', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabase()
    const { data, error } = await supabase
      .from('conversations')
      .select('*')
      .eq('user_id', req.userId!)
      .order('updated_at', { ascending: false })

    if (error) throw error
    res.json({ conversations: data || [] })
  } catch (err: unknown) {
    console.error('List conversations error:', err)
    res.status(500).json({ error: 'Failed to list conversations' })
  }
})

// Create conversation
router.post('/', async (req: AuthRequest, res) => {
  try {
    const { textbook_id } = req.body
    const supabase = getSupabase()

    const { data, error } = await supabase
      .from('conversations')
      .insert({
        user_id: req.userId!,
        title: '新对话',
        current_textbook_id: textbook_id || null,
      })
      .select()
      .single()

    if (error) throw error
    res.json({ conversation: data })
  } catch (err: unknown) {
    console.error('Create conversation error:', err)
    res.status(500).json({ error: 'Failed to create conversation' })
  }
})

// Update conversation (textbook, title)
router.patch('/:id', async (req: AuthRequest, res) => {
  try {
    const { textbook_id, title } = req.body
    const supabase = getSupabase()

    const updates: Record<string, unknown> = {}
    if (textbook_id !== undefined) updates.current_textbook_id = textbook_id
    if (title !== undefined) updates.title = title
    updates.updated_at = new Date().toISOString()

    const { data, error } = await supabase
      .from('conversations')
      .update(updates)
      .eq('id', req.params.id)
      .eq('user_id', req.userId!)
      .select()
      .single()

    if (error) throw error
    res.json({ conversation: data })
  } catch (err: unknown) {
    res.status(500).json({ error: 'Failed to update conversation' })
  }
})

// Get messages for a conversation
router.get('/:id/messages', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabase()
    const { data, error } = await supabase
      .from('messages')
      .select('*')
      .eq('conversation_id', req.params.id)
      .order('created_at', { ascending: true })

    if (error) throw error
    res.json({ messages: data || [] })
  } catch (err: unknown) {
    console.error('Get messages error:', err)
    res.status(500).json({ error: 'Failed to get messages' })
  }
})

// Delete conversation
router.delete('/:id', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabase()
    await supabase
      .from('conversations')
      .delete()
      .eq('id', req.params.id)
      .eq('user_id', req.userId!)

    res.json({ ok: true })
  } catch (err: unknown) {
    res.status(500).json({ error: 'Failed to delete conversation' })
  }
})

export default router
