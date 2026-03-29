import { createClient, SupabaseClient } from '@supabase/supabase-js'

let _client: SupabaseClient | null = null
let _adminClient: SupabaseClient | null = null

export function getSupabase(): SupabaseClient {
  if (_client) return _client
  const url = process.env.SUPABASE_URL
  const anonKey = process.env.SUPABASE_ANON_KEY
  if (!url || !anonKey) throw new Error('SUPABASE_URL and SUPABASE_ANON_KEY must be set')
  _client = createClient(url, anonKey)
  return _client
}

export function getSupabaseAdmin(): SupabaseClient {
  if (_adminClient) return _adminClient
  const url = process.env.SUPABASE_URL
  const serviceKey = process.env.SUPABASE_SERVICE_KEY
  if (!url || !serviceKey) throw new Error('SUPABASE_URL and SUPABASE_SERVICE_KEY must be set')
  _adminClient = createClient(url, serviceKey)
  return _adminClient
}
