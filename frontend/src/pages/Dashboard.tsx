import { useState, useEffect, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'
import { apiFetch } from '../lib/supabase'
import ChatBox from '../components/ChatBox'
import Sidebar from '../components/Sidebar'
import TopBar from '../components/TopBar'
import styles from './Dashboard.module.css'

export interface Message {
  id: string
  role: 'user' | 'assistant' | 'system'
  character?: 'mu' | 'sang' | null
  content: string
  created_at: string
}

export interface Conversation {
  id: string
  title: string
  current_textbook_id?: string
  created_at: string
  updated_at: string
}

export interface Textbook {
  id: string
  filename: string
  file_size: number
  created_at: string
}

export default function Dashboard() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  const [conversations, setConversations] = useState<Conversation[]>([])
  const [activeConversationId, setActiveConversationId] = useState<string | null>(null)
  const [messages, setMessages] = useState<Message[]>([])
  const [textbooks, setTextbooks] = useState<Textbook[]>([])
  const [currentTextbook, setCurrentTextbook] = useState<string | null>(null)
  const [loadingMessages, setLoadingMessages] = useState(false)
  const [sidebarOpen, setSidebarOpen] = useState(true)

  const messagesEndRef = useRef<HTMLDivElement>(null)

  // Load initial data
  useEffect(() => {
    loadConversations()
    loadTextbooks()
  }, [])

  // Load messages when conversation changes
  useEffect(() => {
    if (activeConversationId) {
      loadMessages(activeConversationId)
    } else {
      setMessages([])
    }
  }, [activeConversationId])

  // Auto-scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  async function loadConversations() {
    try {
      const data = await apiFetch('/conversations')
      setConversations(data.conversations || [])
      // Auto-select most recent conversation
      if (data.conversations?.length > 0 && !activeConversationId) {
        setActiveConversationId(data.conversations[0].id)
        const conv = data.conversations[0]
        setCurrentTextbook(conv.current_textbook_id || null)
      }
    } catch (err) {
      console.error('Failed to load conversations:', err)
    }
  }

  async function loadTextbooks() {
    try {
      const data = await apiFetch('/textbooks')
      setTextbooks(data.textbooks || [])
    } catch (err) {
      console.error('Failed to load textbooks:', err)
    }
  }

  async function loadMessages(conversationId: string) {
    setLoadingMessages(true)
    try {
      const data = await apiFetch(`/conversations/${conversationId}/messages`)
      setMessages(data.messages || [])
    } catch (err) {
      console.error('Failed to load messages:', err)
    } finally {
      setLoadingMessages(false)
    }
  }

  async function handleSendMessage(text: string) {
    if (!text.trim()) return

    // Create conversation if none exists
    let convId = activeConversationId
    if (!convId) {
      const data = await apiFetch('/conversations', {
        method: 'POST',
        body: JSON.stringify({ textbook_id: currentTextbook }),
      })
      const newConv: Conversation = data.conversation
      setConversations(prev => [newConv, ...prev])
      setActiveConversationId(newConv.id)
      convId = newConv.id
    }

    // Optimistically add user message
    const tempId = `temp-${Date.now()}`
    const userMsg: Message = {
      id: tempId,
      role: 'user',
      character: null,
      content: text,
      created_at: new Date().toISOString(),
    }
    setMessages(prev => [...prev, userMsg])

    try {
      const data = await apiFetch('/chat', {
        method: 'POST',
        body: JSON.stringify({ conversation_id: convId, message: text }),
      })

      // Replace temp message with server response and add AI response
      const serverUserMsg = data.user_message as Message
      const assistantMsg: Message = data.reply as Message

      setMessages(prev => {
        const filtered = prev.filter(m => m.id !== tempId)
        const withUser = serverUserMsg ? [...filtered, serverUserMsg] : filtered
        return assistantMsg ? [...withUser, assistantMsg] : withUser
      })

      if (data.sessionEnded) {
        // Reload character states after session ends
      }
    } catch (err: unknown) {
      const errorMsg: Message = {
        id: `error-${Date.now()}`,
        role: 'assistant',
        character: null,
        content: `发送失败: ${(err as Error).message}`,
        created_at: new Date().toISOString(),
      }
      setMessages(prev => [...prev.filter(m => m.id !== tempId), errorMsg])
    }
  }

  async function handleNewConversation() {
    const data = await apiFetch('/conversations', {
      method: 'POST',
      body: JSON.stringify({ textbook_id: currentTextbook }),
    })
    const newConv: Conversation = data.conversation
    setConversations(prev => [newConv, ...prev])
    setActiveConversationId(newConv.id)
    setCurrentTextbook(newConv.current_textbook_id || null)
    setMessages([])
  }

  async function handleSelectConversation(convId: string) {
    setActiveConversationId(convId)
    const conv = conversations.find(c => c.id === convId)
    if (conv) {
      setCurrentTextbook(conv.current_textbook_id || null)
    }
  }

  async function handleDeleteConversation(convId: string) {
    if (!confirm('确定删除这段对话？')) return
    await apiFetch(`/conversations/${convId}`, { method: 'DELETE' })
    setConversations(prev => prev.filter(c => c.id !== convId))
    if (activeConversationId === convId) {
      const remaining = conversations.filter(c => c.id !== convId)
      if (remaining.length > 0) {
        setActiveConversationId(remaining[0].id)
      } else {
        setActiveConversationId(null)
        setMessages([])
      }
    }
  }

  async function handleSelectTextbook(textbookId: string) {
    setCurrentTextbook(textbookId)
    if (activeConversationId) {
      await apiFetch(`/conversations/${activeConversationId}`, {
        method: 'PATCH',
        body: JSON.stringify({ textbook_id: textbookId }),
      })
    }
  }

  async function handleUploadTextbook(file: File) {
    const formData = new FormData()
    formData.append('textbook', file)
    const data = await apiFetch('/textbooks/upload', {
      method: 'POST',
      body: formData,
    })
    const newTb: Textbook = data.textbook
    setTextbooks(prev => [...prev, newTb])
    if (!currentTextbook) {
      handleSelectTextbook(newTb.id)
    }
  }

  async function handleDeleteTextbook(textbookId: string) {
    if (!confirm('确定删除这本教材？')) return
    await apiFetch(`/textbooks/${textbookId}`, { method: 'DELETE' })
    setTextbooks(prev => prev.filter(t => t.id !== textbookId))
    if (currentTextbook === textbookId) {
      setCurrentTextbook(null)
    }
  }

  async function handleEndSession() {
    if (!confirm('确定要结束今天的学习吗？系统将生成日记并更新进度。')) return
    // Send end-of-session trigger
    await handleSendMessage('结束当天的学习')
  }

  return (
    <div className={styles.layout}>
      {/* Sidebar */}
      <Sidebar
        open={sidebarOpen}
        conversations={conversations}
        activeConversationId={activeConversationId}
        textbooks={textbooks}
        currentTextbook={currentTextbook}
        onSelectConversation={handleSelectConversation}
        onNewConversation={handleNewConversation}
        onDeleteConversation={handleDeleteConversation}
        onSelectTextbook={handleSelectTextbook}
        onUploadTextbook={handleUploadTextbook}
        onDeleteTextbook={handleDeleteTextbook}
        onEndSession={handleEndSession}
        onToggle={() => setSidebarOpen(o => !o)}
      />

      {/* Main area */}
      <div className={`${styles.main} ${sidebarOpen ? '' : styles.mainFull}`}>
        <TopBar
          onToggleSidebar={() => setSidebarOpen(o => !o)}
          sidebarOpen={sidebarOpen}
        />
        <ChatBox
          messages={messages}
          loading={loadingMessages}
          onSendMessage={handleSendMessage}
          messagesEndRef={messagesEndRef}
        />
      </div>
    </div>
  )
}
