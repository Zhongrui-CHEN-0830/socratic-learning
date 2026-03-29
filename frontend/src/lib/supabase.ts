import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL as string
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY as string

export const supabase = createClient(supabaseUrl, supabaseAnonKey)

// Auth helper
export const getAuthToken = () => localStorage.getItem('auth_token')

export const setAuthToken = (token: string) => {
  localStorage.setItem('auth_token', token)
}

export const clearAuthToken = () => {
  localStorage.removeItem('auth_token')
}

// API helper with auth
export async function apiFetch(endpoint: string, options: RequestInit = {}) {
  const token = getAuthToken()
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(options.headers as Record<string, string> || {}),
  }
  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }

  const res = await fetch(`/api${endpoint}`, {
    ...options,
    headers,
  })

  if (res.status === 401) {
    clearAuthToken()
    window.location.href = '/login'
    throw new Error('Unauthorized')
  }

  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: 'Request failed' }))
    throw new Error(err.error || `HTTP ${res.status}`)
  }

  return res.json()
}
