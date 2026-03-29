import { Router } from 'express'
import { getSupabaseAdmin, getSupabase } from '../lib/supabase.js'
import { generateToken } from '../middleware/auth.js'

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
  } catch (err: unknown) {
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
  } catch (err: unknown) {
    console.error('Login error:', err)
    res.status(500).json({ error: '服务器错误' })
  }
})

router.get('/me', async (req, res) => {
  const { AuthRequest } = await import('../middleware/auth.js')
  const authReq = req as AuthRequest
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
