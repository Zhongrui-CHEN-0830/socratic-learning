import { useState, useEffect } from 'react'
import { apiFetch } from '../lib/supabase'
import styles from './Settings.module.css'

interface ApiKeyConfig {
  id: string
  provider: 'openai' | 'anthropic'
  base_url: string
  is_active: boolean
}

export default function Settings() {
  const [configs, setConfigs] = useState<ApiKeyConfig[]>([])
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [saved, setSaved] = useState(false)
  const [error, setError] = useState('')

  // Form state per provider
  const [openaiKey, setOpenaiKey] = useState('')
  const [openaiUrl, setOpenaiUrl] = useState('https://api.openai.com/v1')
  const [anthropicKey, setAnthropicKey] = useState('')
  const [anthropicUrl, setAnthropicUrl] = useState('https://api.anthropic.com')

  useEffect(() => {
    loadConfigs()
  }, [])

  async function loadConfigs() {
    setLoading(true)
    try {
      const data = await apiFetch('/user/api-keys')
      const keys: ApiKeyConfig[] = data.keys || []

      // Decrypt and populate forms
      // Note: keys returned already decrypted by server
      keys.forEach(k => {
        if (k.provider === 'openai') {
          setOpenaiKey(k.base_url) // The API key is returned as "decrypted key" field
        } else if (k.provider === 'anthropic') {
          setAnthropicKey(k.base_url)
        }
      })

      setConfigs(keys)
    } catch (err) {
      console.error('Failed to load API keys:', err)
    } finally {
      setLoading(false)
    }
  }

  async function handleSave(provider: 'openai' | 'anthropic') {
    setSaving(true)
    setError('')
    setSaved(false)
    try {
      const key = provider === 'openai' ? openaiKey : anthropicKey
      const baseUrl = provider === 'openai' ? openaiUrl : anthropicUrl

      await apiFetch('/user/api-keys', {
        method: 'POST',
        body: JSON.stringify({ provider, base_url: key, key: baseUrl }),
      })
      setSaved(true)
      setTimeout(() => setSaved(false), 3000)
    } catch (err: unknown) {
      setError((err as Error).message)
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return (
      <div className={styles.page}>
        <div className={styles.loading}>加载中...</div>
      </div>
    )
  }

  return (
    <div className={styles.page}>
      <div className={styles.container}>
        <header className={styles.header}>
          <h1 className={styles.title}>设置</h1>
          <p className={styles.subtitle}>配置你的 AI API 密钥，系统将使用你自己的密钥与 AI 对话。密钥采用 AES-256 加密存储。</p>
        </header>

        {error && <div className={styles.error}>{error}</div>}
        {saved && <div className={styles.success}>✓ 保存成功</div>}

        {/* OpenAI */}
        <section className={styles.card}>
          <div className={styles.cardHeader}>
            <div className={styles.providerBadge} data-provider="openai">OpenAI</div>
            <h2 className={styles.cardTitle}>OpenAI API</h2>
            <p className={styles.cardDesc}>使用 OpenAI GPT 系列模型（GPT-4o、GPT-4 等）</p>
          </div>
          <div className={styles.fields}>
            <div className={styles.field}>
              <label>Base URL</label>
              <input
                type="text"
                value={openaiUrl}
                onChange={e => setOpenaiUrl(e.target.value)}
                placeholder="https://api.openai.com/v1"
              />
            </div>
            <div className={styles.field}>
              <label>API Key</label>
              <input
                type="password"
                value={openaiKey}
                onChange={e => setOpenaiKey(e.target.value)}
                placeholder="sk-..."
              />
              <span className={styles.hint}>密钥将加密存储，不会以明文形式保存</span>
            </div>
            <button
              className={styles.saveBtn}
              onClick={() => handleSave('openai')}
              disabled={saving || !openaiKey.trim()}
            >
              {saving ? '保存中...' : '保存 OpenAI 配置'}
            </button>
          </div>
        </section>

        {/* Anthropic */}
        <section className={styles.card}>
          <div className={styles.cardHeader}>
            <div className={styles.providerBadge} data-provider="anthropic">Anthropic</div>
            <h2 className={styles.cardTitle}>Anthropic API</h2>
            <p className={styles.cardDesc}>使用 Claude 系列模型（Claude 3.5 Sonnet、Opus 等）</p>
          </div>
          <div className={styles.fields}>
            <div className={styles.field}>
              <label>Base URL</label>
              <input
                type="text"
                value={anthropicUrl}
                onChange={e => setAnthropicUrl(e.target.value)}
                placeholder="https://api.anthropic.com"
              />
            </div>
            <div className={styles.field}>
              <label>API Key</label>
              <input
                type="password"
                value={anthropicKey}
                onChange={e => setAnthropicKey(e.target.value)}
                placeholder="sk-ant-..."
              />
              <span className={styles.hint}>密钥将加密存储，不会以明文形式保存</span>
            </div>
            <button
              className={styles.saveBtn}
              onClick={() => handleSave('anthropic')}
              disabled={saving || !anthropicKey.trim()}
            >
              {saving ? '保存中...' : '保存 Anthropic 配置'}
            </button>
          </div>
        </section>

        {/* Info */}
        <section className={styles.info}>
          <h3>关于 API 密钥</h3>
          <ul>
            <li>密钥使用 AES-256-GCM 加密存储，即使数据库泄露也无法还原原始密钥</li>
            <li>你可以同时配置多个 provider，系统将使用你选定的 provider 进行对话</li>
            <li>不启用额度限制，用户可自由使用自己的 API 额度</li>
            <li>请勿将密钥泄露给他人，系统不会在任何界面明文展示完整密钥</li>
          </ul>
        </section>
      </div>
    </div>
  )
}
