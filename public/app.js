const messagesEl = document.getElementById('messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const textbookListEl = document.getElementById('textbook-list');
const currentTextbookEl = document.getElementById('current-textbook');
const uploadInput = document.getElementById('upload-input');

// Auto-resize textarea
userInput.addEventListener('input', () => {
  userInput.style.height = 'auto';
  userInput.style.height = Math.min(userInput.scrollHeight, 120) + 'px';
});

// Enter to send (Shift+Enter for newline)
userInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// Load textbooks on start
loadTextbooks();

async function loadTextbooks() {
  const res = await fetch('/api/textbooks');
  const data = await res.json();
  textbookListEl.innerHTML = '';
  data.textbooks.forEach(name => {
    const div = document.createElement('div');
    div.className = 'textbook-item' + (name === data.current ? ' active' : '');
    div.textContent = name.replace('.md', '');
    div.onclick = () => selectTextbook(name);
    textbookListEl.appendChild(div);
  });
  if (data.current) {
    currentTextbookEl.textContent = data.current.replace('.md', '');
  }
}

async function selectTextbook(filename) {
  await fetch('/api/select-textbook', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ filename }),
  });
  currentTextbookEl.textContent = filename.replace('.md', '');
  loadTextbooks();
}

// Upload textbook
uploadInput.addEventListener('change', async (e) => {
  const file = e.target.files[0];
  if (!file) return;
  const formData = new FormData();
  formData.append('textbook', file);
  await fetch('/api/upload', { method: 'POST', body: formData });
  uploadInput.value = '';
  loadTextbooks();
  addSystemMessage(`教材 "${file.name}" 已上传`);
});

// Send message
async function sendMessage() {
  const text = userInput.value.trim();
  if (!text) return;

  userInput.value = '';
  userInput.style.height = 'auto';
  sendBtn.disabled = true;

  addMessage('user', text);
  const loadingEl = addLoading();

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    loadingEl.remove();

    if (data.error) {
      addSystemMessage('错误: ' + data.error);
    } else {
      addMessage('assistant', data.reply);
      if (data.sessionEnded) {
        addSystemMessage('今天的学习已结束。日记和进度已更新。');
      }
    }
  } catch (err) {
    loadingEl.remove();
    addSystemMessage('网络错误: ' + err.message);
  }

  sendBtn.disabled = false;
  userInput.focus();
}

function addMessage(role, content) {
  const div = document.createElement('div');
  div.className = 'message ' + role;

  if (role === 'assistant') {
    div.innerHTML = renderAssistantMessage(content);
  } else {
    div.textContent = content;
  }

  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;

  // Render math
  if (typeof renderMathInElement !== 'undefined') {
    renderMathInElement(div, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false },
      ],
      throwOnError: false,
    });
  }
}

function renderAssistantMessage(text) {
  // Split by character markers
  const parts = text.split(/(【慕千汐】|【桑稚】)/g);
  let html = '';
  let currentChar = '';

  for (const part of parts) {
    if (part === '【慕千汐】') {
      currentChar = 'mu';
      html += '<span class="char-name mu">慕千汐</span>';
    } else if (part === '【桑稚】') {
      currentChar = 'sang';
      html += '<span class="char-name sang">桑稚</span>';
    } else if (part.trim()) {
      // Render action descriptions in parentheses as italic
      let processed = part.replace(/（([^）]+)）/g, '<span class="action">（$1）</span>');
      // Basic markdown: bold, italic, code
      processed = processed.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
      processed = processed.replace(/\*(.+?)\*/g, '<em>$1</em>');
      processed = processed.replace(/`([^`]+)`/g, '<code>$1</code>');
      // Line breaks
      processed = processed.replace(/\n/g, '<br>');
      html += processed;
    }
  }

  return html || text.replace(/\n/g, '<br>');
}

function addSystemMessage(text) {
  const div = document.createElement('div');
  div.className = 'system-msg';
  div.textContent = text;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function addLoading() {
  const div = document.createElement('div');
  div.className = 'loading';
  div.innerHTML = '<span></span><span></span><span></span>';
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return div;
}

// Tool functions
async function viewDiary() {
  const res = await fetch('/api/diary');
  const data = await res.json();
  showModal('学习日记', data.content);
}

async function viewProgress() {
  const res = await fetch('/api/progress');
  const data = await res.json();
  showModal('学习进度', data.content);
}

async function viewNotes() {
  const res = await fetch('/api/textbook-notes');
  const data = await res.json();
  showModal('教材改进笔记', data.content);
}

async function endStudy() {
  if (!confirm('确定要结束今天的学习吗？系统将生成日记并更新进度。')) return;
  sendBtn.disabled = true;
  const loadingEl = addLoading();

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: '结束当天的学习' }),
    });
    const data = await res.json();
    loadingEl.remove();
    addMessage('assistant', data.reply);
    addSystemMessage('今天的学习已结束。日记和进度已更新。');
  } catch (err) {
    loadingEl.remove();
    addSystemMessage('结算失败: ' + err.message);
  }

  sendBtn.disabled = false;
}

async function newSession() {
  if (!confirm('确定要新建对话吗？当前对话历史将被清除。')) return;
  await fetch('/api/new-session', { method: 'POST' });
  messagesEl.innerHTML = '';
  addSystemMessage('新对话已开始。');
}

function showModal(title, content) {
  document.getElementById('modal-title').textContent = title;
  document.getElementById('modal-body').textContent = content;
  document.getElementById('modal').classList.add('active');
}

function closeModal(e) {
  if (e.target === document.getElementById('modal')) {
    document.getElementById('modal').classList.remove('active');
  }
}
