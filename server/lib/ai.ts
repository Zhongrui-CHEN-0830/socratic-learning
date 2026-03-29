import OpenAI from 'openai'
import Anthropic from '@anthropic-ai/sdk'

export interface AIConfig {
  provider: 'openai' | 'anthropic'
  baseUrl: string
  apiKey: string
}

export interface ChatOptions {
  config: AIConfig
  systemPrompt: string
  messages: { role: 'user' | 'assistant'; content: string }[]
  maxTokens?: number
}

export async function chatWithAI({ config, systemPrompt, messages, maxTokens = 4096 }: ChatOptions): Promise<string> {
  if (config.provider === 'anthropic') {
    return chatAnthropic({ config, systemPrompt, messages, maxTokens })
  } else {
    return chatOpenAI({ config, systemPrompt, messages, maxTokens })
  }
}

async function chatOpenAI({ config, systemPrompt, messages, maxTokens }: {
  config: AIConfig; systemPrompt: string; messages: { role: 'user' | 'assistant'; content: string }[]; maxTokens?: number
}): Promise<string> {
  const client = new OpenAI({
    apiKey: config.apiKey,
    baseURL: config.baseUrl || 'https://api.openai.com/v1',
  })

  const allMessages: OpenAI.Chat.ChatCompletionMessageParam[] = [
    { role: 'system', content: systemPrompt },
    ...messages.map(m => ({ role: m.role as 'user' | 'assistant', content: m.content })),
  ]

  const response = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: allMessages,
    max_tokens: maxTokens ?? 4096,
  })

  return response.choices[0]?.message?.content || ''
}

async function chatAnthropic({ config, systemPrompt, messages, maxTokens }: {
  config: AIConfig; systemPrompt: string; messages: { role: 'user' | 'assistant'; content: string }[]; maxTokens?: number
}): Promise<string> {
  const client = new Anthropic({
    apiKey: config.apiKey,
    baseURL: config.baseUrl || undefined,
  })

  const response = await client.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: maxTokens ?? 4096,
    system: systemPrompt,
    messages: messages as Anthropic.MessageCreateParams.Message[],
  })

  return response.content
    .filter(block => block.type === 'text')
    .map(block => (block as { type: 'text'; text: string }).text)
    .join('')
}
