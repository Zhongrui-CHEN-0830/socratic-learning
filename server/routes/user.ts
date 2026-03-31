import { Router } from 'express'
import { getSupabaseAdmin } from '../lib/supabase.js'
import { encrypt, decrypt, maskKey } from '../lib/encryption.js'
import { authMiddleware, AuthRequest } from '../middleware/auth.js'

const router = Router()
router.use(authMiddleware)

// Get all API keys (decrypted for display)
router.get('/api-keys', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabaseAdmin()
    const { data, error } = await supabase
      .from('api_keys')
      .select('*')
      .eq('user_id', req.userId!)
      .eq('is_active', true)

    if (error) throw error

    // Decrypt each key for display (but mask it)
    const keys = (data || []).map(k => {
      try {
        const decrypted = decrypt(k.encrypted_key, k.iv)
        return {
          id: k.id,
          provider: k.provider,
          base_url: maskKey(decrypted), // Show masked version
          is_active: k.is_active,
          created_at: k.created_at,
        }
      } catch {
        return { id: k.id, provider: k.provider, base_url: '***', is_active: k.is_active }
      }
    })

    res.json({ keys })
  } catch (err: unknown) {
    console.error('Get API keys error:', err)
    res.status(500).json({ error: 'Failed to get API keys' })
  }
})

// Save or update API key
router.post('/api-keys', async (req: AuthRequest, res) => {
  try {
    const { provider, base_url, key, model } = req.body
    if (!provider || !key) {
      res.status(400).json({ error: 'Provider and key are required' })
      return
    }

    const supabase = getSupabaseAdmin()

    // Deactivate all existing active keys (only one active config at a time)
    await supabase
      .from('api_keys')
      .update({ is_active: false })
      .eq('user_id', req.userId!)

    // Encrypt and store
    const { encrypted, iv } = encrypt(key)

    const insertData: Record<string, unknown> = {
      user_id: req.userId!,
      provider,
      base_url: base_url || '',
      encrypted_key: encrypted,
      iv,
      is_active: true,
    }
    // Store model if provided (column may not exist yet — ignore error gracefully)
    if (model) insertData.model = model

    const { data, error } = await supabase
      .from('api_keys')
      .insert(insertData)
      .select()
      .single()

    if (error) throw error

    res.json({
      key: {
        id: data.id,
        provider: data.provider,
        base_url: maskKey(key),
        model: data.model || model || null,
        is_active: data.is_active,
        created_at: data.created_at,
      }
    })
  } catch (err: unknown) {
    console.error('Save API key error:', err)
    res.status(500).json({ error: 'Failed to save API key' })
  }
})

// Delete API key
router.delete('/api-keys/:id', async (req: AuthRequest, res) => {
  try {
    const supabase = getSupabaseAdmin()
    const { error } = await supabase
      .from('api_keys')
      .update({ is_active: false })
      .eq('id', req.params.id)
      .eq('user_id', req.userId!)

    if (error) throw error
    res.json({ ok: true })
  } catch (err: unknown) {
    res.status(500).json({ error: 'Failed to delete API key' })
  }
})

// Update profile
router.put('/profile', async (req: AuthRequest, res) => {
  try {
    const { nickname } = req.body
    const supabase = getSupabaseAdmin()

    const { data, error } = await supabase
      .from('profiles')
      .update({ nickname })
      .eq('id', req.userId!)
      .select()
      .single()

    if (error) throw error
    res.json({ profile: data })
  } catch (err: unknown) {
    res.status(500).json({ error: 'Failed to update profile' })
  }
})

export default router
