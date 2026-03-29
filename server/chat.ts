import Anthropic from '@anthropic-ai/sdk';
import { readTeacherFile, readTextbook } from './files.js';

const client = new Anthropic({
  baseURL: process.env.ANTHROPIC_BASE_URL || undefined,
});

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

let conversationHistory: Message[] = [];
let currentTextbook = '';

export function setTextbook(name: string): void {
  currentTextbook = name;
}

export function getTextbook(): string {
  return currentTextbook;
}

export function clearHistory(): void {
  conversationHistory = [];
}

export function getHistory(): Message[] {
  return conversationHistory;
}

async function buildSystemPrompt(): Promise<string> {
  const [system, story, muQianxi, sangZhi, progress] = await Promise.all([
    readTeacherFile('system.md'),
    readTeacherFile('story-background.md'),
    readTeacherFile('mu-qianxi.md'),
    readTeacherFile('sang-zhi.md'),
    readTeacherFile('progress.md'),
  ]);

  let textbookContent = '';
  if (currentTextbook) {
    textbookContent = await readTextbook(currentTextbook);
    if (textbookContent.length > 80000) {
      textbookContent = textbookContent.slice(0, 80000) + '\n\n[...教材内容过长，已截断...]';
    }
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

---

# 当前学习进度
${progress}

${textbookContent ? `---\n\n# 当前教材内容\n${textbookContent}` : '（尚未选择教材）'}

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

export async function chat(userMessage: string): Promise<string> {
  conversationHistory.push({ role: 'user', content: userMessage });

  const systemPrompt = await buildSystemPrompt();
  const model = process.env.MODEL || 'claude-sonnet-4-20250514';

  console.log(`[chat] model=${model}, system prompt length=${systemPrompt.length} chars`);

  const response = await client.messages.create({
    model,
    max_tokens: 4096,
    system: systemPrompt,
    messages: conversationHistory,
  });

  const assistantMessage = response.content
    .filter(block => block.type === 'text')
    .map(block => (block as { type: 'text'; text: string }).text)
    .join('');

  conversationHistory.push({ role: 'assistant', content: assistantMessage });

  return assistantMessage;
}

export async function generateSettlement(): Promise<{
  diary: string;
  progress: string;
  textbookNotes: string;
  muUpdate: string;
  sangUpdate: string;
  farewell: string;
}> {
  const systemPrompt = await buildSystemPrompt();
  const model = process.env.MODEL || 'claude-sonnet-4-20250514';

  const today = new Date().toLocaleDateString('zh-CN');

  const settlementPrompt = `现在用户说了"结束当天的学习"。请完成以下结算任务，严格按照 JSON 格式输出：

1. farewell: 两位角色的告别场景（总结今天所学、展望明天、自然道晚安），保持角色性格
2. diary: 站在用户（男生，第一人称"我"）的立场写一篇日记，记录今天的学习和生活。要求：逼真、生活化、富有细腻的情感。包含学习成果总结，也包含和两位女生互动的细节。日期：${today}
3. progress: 今日学习进度的 markdown 格式记录（章节、知识点、掌握情况）
4. textbookNotes: 今天教学中发现的教材改进点（如果没有则为空字符串）
5. muUpdate: 慕千汐对用户态度的变化描述（用于追加到人设文档的"动态演变区"）
6. sangUpdate: 桑稚对用户态度的变化描述（用于追加到人设文档的"动态演变区"）

请严格输出以下 JSON 格式（不要包含 markdown 代码块标记）：
{"farewell":"...","diary":"...","progress":"...","textbookNotes":"...","muUpdate":"...","sangUpdate":"..."}`;

  const allMessages: Message[] = [
    ...conversationHistory,
    { role: 'user', content: settlementPrompt },
  ];

  const response = await client.messages.create({
    model,
    max_tokens: 8192,
    system: systemPrompt,
    messages: allMessages,
  });

  const text = response.content
    .filter(block => block.type === 'text')
    .map(block => (block as { type: 'text'; text: string }).text)
    .join('');

  try {
    const jsonMatch = text.match(/\{[\s\S]*\}/);
    if (!jsonMatch) throw new Error('No JSON found in response');
    return JSON.parse(jsonMatch[0]);
  } catch {
    return {
      farewell: text,
      diary: '',
      progress: '',
      textbookNotes: '',
      muUpdate: '',
      sangUpdate: '',
    };
  }
}
