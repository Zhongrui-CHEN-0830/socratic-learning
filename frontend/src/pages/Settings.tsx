import { useState, useEffect } from 'react'
import { apiFetch } from '../lib/supabase'
import styles from './Settings.module.css'

interface ApiKeyConfig {
  id: string
  provider: string
  base_url: string
  model?: string
  is_active: boolean
}

// Preset providers with their default base URLs and models
const PROVIDER_PRESETS: Record<string, { label: string; baseUrl: string; models: string[]; keyPlaceholder: string }> = {
  anthropic: {
    label: 'Anthropic (Claude)',
    baseUrl: 'https://api.anthropic.com',
    models: ['claude-opus-4-5', 'claude-sonnet-4-5', 'claude-haiku-4-5', 'claude-opus-4-20250514', 'claude-sonnet-4-20250514'],
    keyPlaceholder: 'sk-ant-...',
  },
  openai: {
    label: 'OpenAI (GPT)',
    baseUrl: 'https://api.openai.com/v1',
    models: ['gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo', 'gpt-3.5-turbo'],
    keyPlaceholder: 'sk-...',
  },
  deepseek: {
    label: 'DeepSeek',
    baseUrl: 'https://api.deepseek.com/v1',
    models: ['deepseek-chat', 'deepseek-reasoner'],
    keyPlaceholder: 'sk-...',
  },
  zhipu: {
    label: '智谱 GLM (ChatGLM)',
    baseUrl: 'https://open.bigmodel.cn/api/paas/v4',
    models: ['glm-4-plus', 'glm-4-air', 'glm-4-flash', 'glm-4-long'],
    keyPlaceholder: 'your-zhipu-api-key',
  },
  minimax: {
    label: 'MiniMax',
    baseUrl: 'https://api.minimax.chat/v1',
    models: ['MiniMax-Text-01', 'abab6.5s-chat', 'abab5.5-chat'],
    keyPlaceholder: 'your-minimax-api-key',
  },
  moonshot: {
    label: 'Moonshot (Kimi)',
    baseUrl: 'https://api.moonshot.cn/v1',
    models: ['moonshot-v1-8k', 'moonshot-v1-32k', 'moonshot-v1-128k'],
    keyPlaceholder: 'sk-...',
  },
  qwen: {
    label: '通义千问 (Qwen)',
    baseUrl: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    models: ['qwen-max', 'qwen-plus', 'qwen-turbo', 'qwen-long'],
    keyPlaceholder: 'sk-...',
  },
  custom: {
    label: '自定义 / 中转站',
    baseUrl: '',
    models: [],
    keyPlaceholder: 'your-api-key',
  },
}

export default function Settings() {
  const [configs, setConfigs] = useState<ApiKeyConfig[]>([])
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [saved, setSaved] = useState(false)
  const [error, setError] = useState('')

  // Form state
  const [selectedProvider, setSelectedProvider] = useState('anthropic')
  const [apiKey, setApiKey] = useState('')
  const [baseUrl, setBaseUrl] = useState(PROVIDER_PRESETS.anthropic.baseUrl)
  const [selectedModel, setSelectedModel] = useState(PROVIDER_PRESETS.anthropic.models[0])
  const [customModel, setCustomModel] = useState('')

  useEffect(() => {
    loadConfigs()
  }, [])

  // Update baseUrl and model when provider changes
  useEffect(() => {
    const preset = PROVIDER_PRESETS[selectedProvider]
    if (preset) {
      setBaseUrl(preset.baseUrl)
      setSelectedModel(preset.models[0] || '')
      setCustomModel('')
    }
  }, [selectedProvider])

  async function loadConfigs() {
    setLoading(true)
    try {
      const data = await apiFetch('/user/api-keys')
      setConfigs(data.keys || [])
    } catch (err) {
      console.error('Failed to load API keys:', err)
    } finally {
      setLoading(false)
    }
  }

  async function handleSave() {
    if (!apiKey.trim()) {
      setError('请输入 API Key')
      return
    }
    setSaving(true)
    setError('')
    setSaved(false)
    try {
      const model = customModel.trim() || selectedModel
      // provider field: use selectedProvider; for custom, use 'openai' as protocol (OpenAI-compatible)
      const providerForServer = selectedProvider === 'custom' ? 'openai' : selectedProvider
      await apiFetch('/user/api-keys', {
        method: 'POST',
        body: JSON.stringify({
          provider: providerForServer,
          base_url: baseUrl.trim(),
          key: apiKey.trim(),
          model: model || undefined,
        }),
      })
      setSaved(true)
      setTimeout(() => setSaved(false), 3000)
      await loadConfigs()
      setApiKey('')
    } catch (err: unknown) {
      setError((err as Error).message)
    } finally {
      setSaving(false)
    }
  }

  async function handleDelete(id: string) {
    try {
      await apiFetch(`/user/api-keys/${id}`, { method: 'DELETE' })
      await loadConfigs()
    } catch (err: unknown) {
      setError((err as Error).message)
    }
  }

  const preset = PROVIDER_PRESETS[selectedProvider]

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
          <h1 className={styles.title}>API 设置</h1>
          <p className={styles.subtitle}>配置你的 AI API 密钥。支持 Anthropic、OpenAI、DeepSeek、GLM、MiniMax、Kimi、通义千问及任意 OpenAI 兼容中转站。密钥采用 AES-256 加密存储。</p>
        </header>

        {error && <div className={styles.error}>{error}</div>}
        {saved && <div className={styles.success}>✓ 保存成功</div>}

        {/* Add / Update Key */}
        <section className={styles.card}>
          <div className={styles.cardHeader}>
            <h2 className={styles.cardTitle}>添加 / 更新 API 配置</h2>
          </div>
          <div className={styles.fields}>

            {/* Provider selector */}
            <div className={styles.field}>
              <label>服务商</label>
              <select
                value={selectedProvider}
                onChange={e => setSelectedProvider(e.target.value)}
                className={styles.select}
              >
                {Object.entries(PROVIDER_PRESETS).map(([key, p]) => (
                  <option key={key} value={key}>{p.label}</option>
                ))}
              </select>
            </div>

            {/* Base URL */}
            <div className={styles.field}>
              <label>Base URL {selectedProvider === 'custom' ? '（中转站地址）' : ''}</label>
              <input
                type="text"
                value={baseUrl}
                onChange={e => setBaseUrl(e.target.value)}
                placeholder={preset?.baseUrl || 'https://your-proxy.com/v1'}
              />
              {selectedProvider === 'custom' && (
                <span className={styles.hint}>填入中转站的 OpenAI 兼容接口地址，如 https://api.example.com/v1</span>
              )}
            </div>

            {/* Model selector */}
            <div className={styles.field}>
              <label>模型</label>
              {preset?.models.length > 0 ? (
                <select
                  value={selectedModel}
                  onChange={e => setSelectedModel(e.target.value)}
                  className={styles.select}
                >
                  {preset.models.map(m => (
                    <option key={m} value={m}>{m}</option>
                  ))}
                  <option value="__custom__">自定义模型名...</option>
                </select>
              ) : null}
              {(selectedModel === '__custom__' || preset?.models.length === 0) && (
                <input
                  type="text"
                  value={customModel}
                  onChange={e => setCustomModel(e.target.value)}
                  placeholder="输入模型名，如 gpt-4o / claude-opus-4-5 / deepseek-chat"
                  style={{ marginTop: preset?.models.length > 0 ? '8px' : '0' }}
                />
              )}
            </div>

            {/* API Key */}
            <div className={styles.field}>
              <label>API Key</label>
              <input
                type="password"
                value={apiKey}
                onChange={e => setApiKey(e.target.value)}
                placeholder={preset?.keyPlaceholder || 'your-api-key'}
              />
              <span className={styles.hint}>密钥将使用 AES-256-GCM 加密存储，不会明文保存</span>
            </div>

            <button
              className={styles.saveBtn}
              onClick={handleSave}
              disabled={saving || !apiKey.trim()}
            >
              {saving ? '保存中...' : '保存配置'}
            </button>
          </div>
        </section>

        {/* Active configs */}
        {configs.length > 0 && (
          <section className={styles.card}>
            <div className={styles.cardHeader}>
              <h2 className={styles.cardTitle}>已配置的 API</h2>
            </div>
            <div className={styles.configList}>
              {configs.map(c => (
                <div key={c.id} className={styles.configItem}>
                  <div className={styles.configInfo}>
                    <span className={styles.providerBadge} data-provider={c.provider}>
                      {PROVIDER_PRESETS[c.provider]?.label || c.provider}
                    </span>
                    <span className={styles.configKey}>{c.base_url}</span>
                  </div>
                  <button
                    className={styles.deleteConfigBtn}
                    onClick={() => handleDelete(c.id)}
                  >
                    删除
                  </button>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Info */}
        <section className={styles.info}>
          <h3>使用说明</h3>
          <ul>
            <li>支持所有 OpenAI 兼容接口，包括国内中转站（只需填入中转站地址和对应 Key）</li>
            <li>国内模型（DeepSeek、GLM、MiniMax、Kimi、通义千问）均使用 OpenAI 兼容协议</li>
            <li>可以自由选择模型，如 claude-opus-4-5（最强）或 claude-sonnet-4-5（均衡）</li>
            <li>密钥使用 AES-256-GCM 加密存储，即使数据库泄露也无法还原原始密钥</li>
            <li>不设额度限制，你的 API 额度完全由你自己控制</li>
          </ul>
        </section>
      </div>
    </div>
  )
}
