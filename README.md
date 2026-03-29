# 墨韵书院 · 苏格拉底伴学系统

一个具有情感记忆的 AI 驱动学习平台。两位虚拟教师（慕千汐 & 桑稚）会记住你的学习历程、性格弱点和情感变化，陪你完成一场真正的苏格拉底式学习之旅。

![墨韵书院](https://img.shields.io/badge/墨韵书院-苏格拉底伴学-c9a84c?style=for-the-badge)

## 功能特性

- 🎓 **苏格拉底式教学** — AI 教师通过提问引导思考，而非直接给答案
- 💾 **持久化对话** — 所有对话历史永久保存，随时继续学习
- 📚 **多教材支持** — 同时学习多本教材，情感态度跨教材累积
- 💬 **角色记忆系统** — 虚拟教师的情感态度会随学习历程演变，不会重置
- 🔐 **自定义 API 密钥** — 用户填入自己的 OpenAI/Anthropic 密钥，AES-256 加密存储
- 📱 **现代化前端** — 墨韵书院设计美学，深色木质色调

## 技术栈

| 层次 | 技术 |
|------|------|
| 前端 | React 18 + TypeScript + Vite |
| 后端 | Express + TypeScript |
| 数据库 | Supabase PostgreSQL |
| 文件存储 | Supabase Storage |
| 认证 | Supabase Auth + JWT |
| 加密 | AES-256-GCM |

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/YOUR_USERNAME/socratic-learning.git
cd socratic-learning
```

### 2. 配置 Supabase

1. 在 [supabase.com](https://supabase.com) 创建一个免费项目
2. 在 **SQL Editor** 中运行 `sql/migration.sql`
3. 在 **Settings > API** 中获取 `SUPABASE_URL` 和 `SUPABASE_SERVICE_KEY`
4. 在 **Storage** 中创建一个名为 `textbooks` 的 bucket

### 3. 配置环境变量

```bash
cp .env.example server/.env
# 编辑 server/.env 填入 Supabase 凭据和 JWT 密钥
```

前端环境变量（在 GitHub Secrets 中配置）:
```
VITE_SUPABASE_URL=your-supabase-url
VITE_SUPABASE_ANON_KEY=your-supabase-anon-key
```

### 4. 本地开发

```bash
# 前端
cd frontend && npm install && npm run dev

# 后端（新终端）
cd server && npm install && npm run dev
```

打开 http://localhost:5173

### 5. 构建生产版本

```bash
cd frontend && npm run build
# 前端构建到 frontend/dist/
# 然后运行服务器: cd server && npm run dev
```

## 部署到 VPS（Evoxt）

### 自动部署（推荐）

1. 将代码推送到 GitHub
2. 配置 GitHub Secrets:
   - `VPS_HOST` — VPS IP 地址
   - `VPS_USER` — SSH 用户名
   - `VPS_PASSWORD` — SSH 密码
   - `VPS_PORT` — SSH 端口（默认 22）
3. 每次推送到 main 分支自动部署

### 手动部署

```bash
# 1. 在 VPS 上安装 Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# 2. 安装 PM2
sudo npm install -g pm2

# 3. 克隆仓库
git clone https://github.com/YOUR_USERNAME/socratic-learning.git
cd socratic-learning/server

# 4. 配置 .env
cp ../.env.example .env
nano .env  # 填入所有凭据

# 5. 安装依赖并构建
npm install
cd ../frontend && npm install && npm run build

# 6. 用 PM2 启动
pm2 start dist/index.js --name socratic-learning
pm2 save
pm2 startup

# 7. 配置 Nginx（可选，用于 HTTPS）
```

### Nginx 配置示例

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## 项目结构

```
socratic-learning/
├── frontend/              # React 前端
│   ├── src/
│   │   ├── components/    # UI 组件
│   │   ├── pages/        # 页面（Login/Register/Dashboard/Settings）
│   │   ├── contexts/     # React Context（Auth）
│   │   └── lib/          # Supabase 客户端
│   └── dist/             # 构建输出
├── server/                # Express 后端
│   ├── routes/           # API 路由
│   ├── middleware/       # JWT 认证
│   └── lib/              # 加密/AI/Supabase 工具
├── teacher/              # 角色设定文件（本地备份）
├── sql/
│   └── migration.sql     # Supabase 数据库迁移
├── .env.example          # 环境变量模板
└── SPEC.md               # 完整技术规格文档
```

## API 端点

### 认证
- `POST /api/auth/register` — 注册
- `POST /api/auth/login` — 登录
- `GET /api/auth/me` — 当前用户

### 用户
- `GET /api/user/api-keys` — 获取 API 密钥
- `POST /api/user/api-keys` — 保存 API 密钥
- `PUT /api/user/profile` — 更新个人资料

### 教材
- `GET /api/textbooks` — 列表
- `POST /api/textbooks/upload` — 上传
- `GET /api/textbooks/:id/content` — 获取内容
- `DELETE /api/textbooks/:id` — 删除

### 对话
- `GET /api/conversations` — 对话列表
- `POST /api/conversations` — 新建对话
- `PATCH /api/conversations/:id` — 更新对话
- `GET /api/conversations/:id/messages` — 消息历史
- `DELETE /api/conversations/:id` — 删除对话

### 聊天
- `POST /api/chat` — 发送消息

### 角色
- `GET /api/characters/state` — 角色状态（情感值）
- `GET /api/characters/logs` — 态度变化日志

## 数据库架构

核心表：`profiles`（用户）、`api_keys`（加密密钥）、`textbooks`（教材文件）、`conversations`（对话）、`messages`（消息）、`character_states`（角色情感，跨对话全局）、`diaries`（日记）、`progress`（学习进度）

详见 `sql/migration.sql`

## 设计理念

**"墨韵书院 · Academic Inkatecture"**
- 深色木质基调，书房/古籍氛围
- 暖金色点缀
- 慕千汐：冷紫砚色 / 桑稚：暖琥珀色
- 毛笔质感装饰元素

详见 `SPEC.md`
