import { Router } from 'express'
import { getSupabase } from '../lib/supabase.js'
import { decrypt } from '../lib/encryption.js'
import { chatWithAI } from '../lib/ai.js'
import { authMiddleware, AuthRequest } from '../middleware/auth.js'

const router = Router()
router.use(authMiddleware)

// Read teacher character files from local filesystem
async function readTeacherFile(filename: string): Promise<string> {
  try {
    const { promises: fs } = await import('fs')
    const path = await import('path')
    const { fileURLToPath } = await import('url')
    const __dirname = path.dirname(fileURLToPath(import.meta.url))
    const content = await fs.readFile(
      path.join(__dirname, '..', 'teacher', filename),
      'utf-8'
    )
    return content
  } catch {
    return ''
  }
}

// Build system prompt with character states from DB
async function buildSystemPrompt(
  userId: string,
  textbookContent: string
): Promise<string> {
  const [system, story, muQianxi, sangZhi] = await Promise.all([
    readTeacherFile('system.md'),
    readTeacherFile('story-background.md'),
    readTeacherFile('mu-qianxi.md'),
    readTeacherFile('sang-zhi.md'),
  ])

  const supabase = getSupabase()
  const { data: states } = await supabase
    .from('character_states')
    .select('*')
    .eq('user_id', userId)

  const muState = states?.find(s => s.character_id === 'mu')
  const sangState = states?.find(s => s.character_id === 'sang')

  let characterDynamics = ''
  if (muState) {
    const muLog = (muState.log || []).slice(-5).join('\n')
    characterDynamics += `\n## 慕千汐 当前状态\n好感度: ${muState.affection}/100 | 严格度: ${muState.strictness}/100\n最近动态:\n${muLog || '暂无动态'}\n`
  }
  if (sangState) {
    const sangLog = (sangState.log || []).slice(-5).join('\n')
    characterDynamics += `\n## 桑稚 当前状态\n好感度: ${sangState.affection}/100 | 严格度: ${sangState.strictness}/100\n最近动态:\n${sangLog || '暂无动态'}\n`
  }

  let truncatedTextbook = ''
  if (textbookContent) {
    truncatedTextbook = textbookContent.length > 80000
      ? textbookContent.slice(0, 80000) + '\n\n[...教材内容过长，已截断...]'
      : textbookContent
  }

  return `${system}

---

# 故事背景
${story}

---

# 角色：慕千汐
${muQianxi}

---

# 角色：桑稚
${sangZhi}

${characterDynamics}

${textbookContent ? `---\n\n# 当前教材内容\n${truncatedTextbook}` : '（尚未选择教材）'}

---

# 输出格式要求
- 每次回复中，两位角色都应该有发言（除非剧情需要只有一人说话）
- 角色发言用 【慕千汐】 和 【桑稚】 标注
- 动作和表情描写用中文括号包裹，如：（推了推眼镜）
- 数学公式用 LaTeX：行内 $...$ ，独立 $$...$$
- 保持苏格拉底式教学：多提问，少直接给答案
- 每轮推进一个微目标，不要贪多
- 用中文交流`;
}

function detectCharacter(content: string): 'mu' | 'sang' | null {
  if (content.includes('【慕千汐】')) return 'mu'
  if (content.includes('【桑稚】')) return 'sang'
  return null
}

// Get user's active API key
async function getUserAIConfig(userId: string): Promise<{ provider: 'openai' | 'anthropic'; baseUrl: string; apiKey: string } | null> {
  const supabase = getSupabase()
  const { data } = await supabase
    .from('api_keys')
    .select('*')
    .eq('user_id', userId)
    .eq('is_active', true)
    .maybeSingle()

  if (!data) return null

  try {
    const decryptedKey = decrypt(data.encrypted_key, data.iv)
    return {
      provider: data.provider as 'openai' | 'anthropic',
      baseUrl: data.base_url,
      apiKey: decryptedKey,
    }
  } catch {
    return null
  }
}

// Get textbook content
async function getTextbookContent(userId: string, textbookId: string | null): Promise<string> {
  if (!textbookId) return ''
  const supabase = getSupabase()
  const { data } = await supabase
    .from('textbooks')
    .select('storage_path')
    .eq('id', textbookId)
    .eq('user_id', userId)
    .maybeSingle()

  if (!data) return ''

  const { data: fileData } = await supabase.storage
    .from('textbooks')
    .download(data.storage_path)

  return fileData ? await fileData.text() : ''
}

// Main chat endpoint
router.post('/', async (req: AuthRequest, res) => {
  try {
    const { conversation_id, message } = req.body
    if (!message) {
      res.status(400).json({ error: 'Message is required' })
      return
    }

    const supabase = getSupabase()
    const userId = req.userId!

    // Get conversation
    const { data: conv } = await supabase
      .from('conversations')
      .select('*')
      .eq('id', conversation_id)
      .eq('user_id', userId)
      .maybeSingle()

    if (!conv) {
      res.status(404).json({ error: 'Conversation not found' })
      return
    }

    // Load messages for this conversation
    const { data: dbMessages } = await supabase
      .from('messages')
      .select('*')
      .eq('conversation_id', conversation_id)
      .order('created_at', { ascending: true })

    const historyMessages = (dbMessages || []).map(m => ({
      role: m.role as 'user' | 'assistant',
      content: m.content,
    }))

    // Load textbook content
    const textbookContent = await getTextbookContent(userId, conv.current_textbook_id)

    // Get AI config
    const aiConfig = await getUserAIConfig(userId)
    if (!aiConfig) {
      res.status(400).json({ error: '请先在设置中配置 API 密钥' })
      return
    }

    // Build system prompt
    const systemPrompt = await buildSystemPrompt(userId, textbookContent)

    // Handle end-of-session trigger
    if (message.includes('结束当天的学习')) {
      const result = await handleEndSession(userId, conversation_id, historyMessages, systemPrompt, aiConfig)
      res.json({
        reply: result.farewell,
        sessionEnded: true,
        user_message: null,
      })
      return
    }

    // Call AI
    const reply = await chatWithAI({
      config: aiConfig,
      systemPrompt,
      messages: historyMessages,
      maxTokens: 4096,
    })

    // Save user message
    const { data: savedUserMsg } = await supabase
      .from('messages')
      .insert({
        conversation_id,
        role: 'user',
        content: message,
      })
      .select()
      .single()

    // Save assistant message
    const char = detectCharacter(reply)
    const { data: savedAssistantMsg } = await supabase
      .from('messages')
      .insert({
        conversation_id,
        role: 'assistant',
        character: char,
        content: reply,
      })
      .select()
      .single()

    // Update conversation timestamp
    await supabase
      .from('conversations')
      .update({ updated_at: new Date().toISOString() })
      .eq('id', conversation_id)

    res.json({
      reply: savedAssistantMsg,
      user_message: savedUserMsg,
      sessionEnded: false,
    })
  } catch (err: unknown) {
    console.error('Chat error:', err)
    res.status(500).json({ error: (err as Error).message })
  }
})

async function handleEndSession(
  userId: string,
  conversationId: string,
  historyMessages: { role: string; content: string }[],
  systemPrompt: string,
  aiConfig: { provider: 'openai' | 'anthropic'; baseUrl: string; apiKey: string }
): Promise<{ farewell: string }> {
  const today = new Date().toLocaleDateString('zh-CN')

  const settlementPrompt = `现在用户说了"结束当天的学习"。请完成以下结算任务，严格按 JSON 格式输出：

1. farewell: 两位角色的告别场景（总结今天所学、展望明天、自然道晚安），保持角色性格
2. muUpdate: 慕千汐对用户态度的变化描述（一句话，用于追加到态度日志）
3. sangUpdate: 桑稚对用户态度的变化描述（一句话，用于追加到态度日志）
4. diary: 站在用户（男生，第一人称"我"）的立场写一篇日记，记录今天的学习和生活。要求：逼真、生活化、富有细腻的情感。包含学习成果总结，也包含和两位女生互动的细节。日期：${today}

请严格输出以下 JSON 格式（不要包含 markdown 代码块标记）：
{"farewell":"...","muUpdate":"...","sangUpdate":"...","diary":"..."}`

  const allMessages = [
    ...historyMessages,
    { role: 'user' as const, content: settlementPrompt },
  ]

  let farewell = '今天的课程到这里就结束了，我们明天见。'
  let muUpdate = ''
  let sangUpdate = ''

  try {
    const reply = await chatWithAI({
      config: aiConfig,
      systemPrompt,
      messages: allMessages,
      maxTokens: 8192,
    })

    try {
      const jsonMatch = reply.match(/\{[\s\S]*\}/)
      if (jsonMatch) {
        const parsed = JSON.parse(jsonMatch[0])
        farewell = parsed.farewell || farewell
        muUpdate = parsed.muUpdate || ''
        sangUpdate = parsed.sangUpdate || ''

        // Save diary
        if (parsed.diary) {
          const supabase = getSupabase()
          await supabase.from('diaries').insert({
            user_id: userId,
            date: new Date().toISOString().split('T')[0],
            content: parsed.diary,
          })
        }
      }
    } catch { /* ignore parse errors */ }
  } catch { /* ignore AI errors */ }

  // Update character states
  const supabase = getSupabase()
  const timestamp = new Date().toISOString()

  if (muUpdate) {
    try {
      await supabase.rpc('character_append_log', {
        p_user_id: userId,
        p_character_id: 'mu',
        p_entry: muUpdate,
        p_timestamp: timestamp,
      })
    } catch { /* ignore RPC errors */ }
  }

  if (sangUpdate) {
    try {
      await supabase.rpc('character_append_log', {
        p_user_id: userId,
        p_character_id: 'sang',
        p_entry: sangUpdate,
        p_timestamp: timestamp,
      })
    } catch { /* ignore */ }
  }

  // Clear conversation messages for this conversation (keep history in DB for display)
  // Actually don't clear - let user browse history. Just update character state.

  return { farewell }
}
