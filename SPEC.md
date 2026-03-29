# 苏格拉底伴学系统 — 技术规格文档 v1.0

## 1. Concept & Vision

**核心理念**：一个具有灵魂的 AI 伴学平台。两位虚拟教师（慕千汐 & 桑稚）不是冰冷的 AI 回复容器，而是有情感、有记忆、有个性发展的真实学习伙伴。系统模拟真实的师生关系——教师会记住你的弱点、你的进步、你在学习中流露的情绪，并据此调整教学方式。

**设计美学**：**"墨韵书院 · Academic Inkatecture"**
- 深色木质基调（书房/古籍氛围），不是科技感冷调
- 暖金色点缀，砚台紫色 × 桑稚琥珀色 的角色系统
- 中文衬线标题 + 现代无衬线正文
- 毛笔质感装饰元素，但整体克制，留白充足

## 2. Design Language

### 色彩系统
```css
--ink-black: #1a1612;        /* 主背景，深墨色 */
--ink-dark: #242019;         /* 次级背景 */
--ink-surface: #2e2a23;      /* 卡片/面板 */
--ink-border: #3d3830;       /* 边框 */
--gold-accent: #c9a84c;     /* 暖金色强调 */
--gold-muted: #8a7040;      /* 暖金色次要 */
--mu-primary: #9b7fba;       /* 慕千汐：冷紫砚色 */
--mu-bg: #2a2235;           /* 慕千汐：气泡背景 */
--sang-primary: #d4956a;     /* 桑稚：暖琥珀色 */
--sang-bg: #352a20;         /* 桑稚：气泡背景 */
--text-primary: #e8e0d4;     /* 主文字，暖白 */
--text-secondary: #9a9080;   /* 次要文字 */
--text-muted: #6a6258;      /* 弱化文字 */
--danger: #c0614a;          /* 危险/错误 */
--success: #6a9e6a;         /* 成功 */
```

### 字体
- 标题：`"Noto Serif SC"`（中文衬线，学术感）
- 正文：`"Noto Sans SC"`（中文无衬线，可读性）
- 代码/公式：`"JetBrains Mono"`（等宽）

### 间距系统
- Base unit: 4px
- 大量留白：section gap ≥ 32px
- 卡片内 padding: 20–24px
- 消息气泡 padding: 14–18px

### 动效
- 页面进入：fade + translateY(12px)，400ms ease-out，元素错开 80ms
- 消息出现：fade + scale(0.97→1)，300ms ease-out
- 按钮 hover：subtle glow + translateY(-1px)，200ms
- 加载动画：三颗墨点跳动（改编自原来的 bounce）

## 3. Layout & Structure

### 页面结构
```
/             → 重定向到 /login 或 /app
/login        → 登录页（居中卡片，深色背景+装饰图案）
/register     → 注册页（与登录视觉统一）
/app          → 主界面（左侧边栏 + 主内容区）
/app/settings → 设置页（API密钥、个人偏好）
```

### App 主界面布局
```
┌──────────────────────────────────────────────────┐
│  顶栏：Logo + 当前对话标题 + 用户菜单             │
├────────────┬─────────────────────────────────────┤
│            │                                     │
│  左侧边栏  │         主内容区                     │
│  260px     │                                     │
│            │  ┌─────────────────────────────┐   │
│  · 教材列表 │  │  对话消息流                  │   │
│  · 上传    │  │                             │   │
│  · 工具    │  │                             │   │
│  · 对话列表 │  └─────────────────────────────┘   │
│            │                                     │
│            │  ┌─────────────────────────────┐   │
│            │  │  输入框                       │   │
│            │  └─────────────────────────────┘   │
└────────────┴─────────────────────────────────────┘
```

### 响应式策略
- Desktop（>1024px）：完整侧边栏
- Tablet（768–1024px）：侧边栏可折叠
- Mobile（<768px）：底部 tab 导航，侧边栏变为 drawer

## 4. Features & Interactions

### 4.1 认证系统
- **注册**：邮箱 + 密码（≥8位），Supabase Auth
- **登录**：邮箱 + 密码，JWT token 存 localStorage
- **登出**：清除 token，重定向到登录页
- **错误处理**：邮箱格式错误、密码过短、已注册邮箱、凭据错误

### 4.2 教材系统
- **上传**：支持 .md 文件，存 Supabase Storage
- **选择**：点击切换当前教材，触发 AI context 更新
- **状态**：当前激活教材高亮显示
- **删除**：长按/右键删除（需确认）

### 4.3 对话系统
- **新建对话**：创建新 conversation（保留历史所有对话）
- **对话列表**：侧边栏展示所有对话，按时间倒序
- **切换对话**：点击切换，消息流刷新
- **消息展示**：角色气泡区分，数学公式渲染（KaTeX）
- **历史加载**：进入对话时自动加载历史消息

### 4.4 情感系统（核心创新）
**设计原则**：虚拟教师的情感态度是**全局的、累积的**，跨教材、跨对话共享。

**角色状态表**（`character_states`）：
```
user_id, character_id, 
affection: 0-100       // 好感度
strictness: 0-100     // 严格程度  
mood: JSON            // 当前情绪状态
log: JSON[]           // 态度变化历史（追加，不可覆盖）
```

**更新规则**：
- 每次对话结束（"结束当天学习"）→ 结算时 AI 决定态度变化
- 切换教材时 → 态度不变，保持连续
- 新建对话 → 态度不变

### 4.5 API 密钥管理
- 用户填入：Provider（OpenAI/Anthropic）+ Base URL + API Key
- **加密存储**：后端使用 AES-256-GCM 加密后存 DB
- **使用**：发消息时后端解密，用于构建 AI 请求
- **显示**：密钥以 `sk-***...` 形式部分展示

### 4.6 日记 & 进度
- **日记**：AI 生成，用户可查看历史
- **进度**：按教材章节记录，已掌握/待巩固标注

### 4.7 结束学习结算
- 用户说"结束当天的学习" → 触发完整结算流程：
  1. AI 生成告别语
  2. 生成日记（第一人称）
  3. 更新学习进度
  4. 更新角色情感状态
  5. 清空当前对话 history（conversation_messages）

## 5. Component Inventory

### 5.1 `<AuthPage>`
- 居中卡片，含 logo、标题、表单
- 背景：深色 + 微妙的几何装饰图案（SVG）
- 状态：idle / loading / error
- 错误时卡片轻微 shake 动画

### 5.2 `<AppLayout>`
- 顶栏 + 侧边栏 + 主内容区三栏布局
- 顶栏：左侧 logo，右侧用户 avatar + dropdown
- 侧边栏可折叠，mobile 时为 drawer

### 5.3 `<Sidebar>`
- 教材列表（可选择、上传、删除）
- 工具按钮组（查看日记/进度/笔记）
- 对话列表（按时间倒序，可切换/删除）
- 结束学习按钮（醒目红色）

### 5.4 `<ChatBox>`
- 消息列表，支持虚拟滚动（大量消息时）
- 消息气泡：用户右/AI左，颜色区分角色
- 角色名称标签：千汐紫色 / 桑稚琥珀色
- 动作描写：斜体灰色
- 数学公式：KaTeX 渲染
- 加载动画：三墨点

### 5.5 `<InputArea>`
- Textarea 自动高度（最大 120px）
- Enter 发送，Shift+Enter 换行
- 发送时 disabled + loading 状态

### 5.6 `<Settings>`
- API 密钥配置卡片（OpenAI / Anthropic）
- 每个 provider：启用开关 + Base URL + API Key
- 保存时加密传输

### 5.7 `<Modal>`
- 全局通用模态框
- 用于查看日记/进度/笔记
- 点击背景关闭

## 6. Technical Approach

### 前端
- **框架**：React 18 + TypeScript + Vite
- **路由**：React Router v6
- **状态**：React Context（AuthContext, ChatContext）
- **样式**：CSS Modules + CSS Variables（不用 Tailwind）
- **AI 渲染**：KaTeX（数学公式）
- **HTTP**：fetch（不用 axios，轻量）

### 后端（Express）
- **认证**：jsonwebtoken（JWT）+ bcrypt
- **加密**：crypto (AES-256-GCM) 存密钥
- **AI 调用**：OpenAI SDK / Anthropic SDK（按用户配置动态选择）
- **Supabase**：Server-side SDK（Admin key）

### 数据库（Supabase PostgreSQL）

```sql
-- 用户配置（扩展 Auth）
create table profiles (
  id uuid references auth.users primary key,
  email text unique not null,
  nickname text,
  created_at timestamptz default now()
);

-- API 密钥（加密存储）
create table api_keys (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id) on delete cascade,
  provider text check (provider in ('openai', 'anthropic')),
  base_url text default 'https://api.openai.com',
  encrypted_key text not null,
  iv text not null,
  is_active boolean default true,
  created_at timestamptz default now()
);

-- 教材文件
create table textbooks (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id) on delete cascade,
  filename text not null,
  storage_path text not null,
  file_size bigint,
  created_at timestamptz default now()
);

-- 对话会话
create table conversations (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id) on delete cascade,
  title text,  -- AI 生成或用户自定义
  current_textbook_id uuid references textbooks(id),
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- 消息记录
create table messages (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid references conversations(id) on delete cascade,
  role text check (role in ('user', 'assistant', 'system')),
  character text check (character in ('mu', 'sang', null)), -- AI 回复时标记角色
  content text not null,
  created_at timestamptz default now()
);

-- 角色情感状态（跨对话全局）
create table character_states (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id) on delete cascade,
  character_id text not null, -- 'mu' | 'sang' | 其他可扩展角色
  affection integer default 50,
  strictness integer default 50,
  mood JSONB default '{}',
  log JSONB default '[]',  -- 态度变化历史
  updated_at timestamptz default now(),
  unique(user_id, character_id)
);

-- 日记
create table diaries (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id) on delete cascade,
  date date not null,
  content text not null,
  created_at timestamptz default now()
);

-- 学习进度
create table progress (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id) on delete cascade,
  textbook_id uuid references textbooks(id),
  conversation_id uuid references conversations(id),
  chapter text,
  notes text,
  mastery text check (mastery in ('new', 'learning', 'mastered')),
  created_at timestamptz default now()
);
```

### API Endpoints

```
Auth:
  POST   /api/auth/register     { email, password }
  POST   /api/auth/login        { email, password } → { token }
  GET    /api/auth/me           [JWT] → profile

User:
  GET    /api/user/api-keys     [JWT] → api_keys (解密后)
  POST   /api/user/api-keys     [JWT] { provider, base_url, key }
  DELETE /api/user/api-keys/:id [JWT]
  PUT    /api/user/profile      [JWT] { nickname }

Textbooks:
  GET    /api/textbooks         [JWT] → textbooks
  POST   /api/textbooks/upload  [JWT] + multipart
  DELETE /api/textbooks/:id     [JWT]

Conversations:
  GET    /api/conversations     [JWT] → conversations
  POST   /api/conversations     [JWT] { textbook_id? } → conversation
  DELETE /api/conversations/:id [JWT]

Messages:
  GET    /api/conversations/:id/messages [JWT]
  POST   /api/chat              [JWT] { conversation_id, message }

Characters:
  GET    /api/characters/state [JWT] → character_states
  GET    /api/characters/logs  [JWT] → character log history

Diary:
  GET    /api/diaries           [JWT] → diaries

Progress:
  GET    /api/progress          [JWT] { textbook_id? }
```

### 部署架构
```
GitHub Repository → GitHub Actions (可选) 
                        ↓
              VPS (pm2 process manager)
                  ↓
              Express Server (:3000)
              + nginx (SSL, port 80/443)
              + 域名解析到 VPS IP
```
