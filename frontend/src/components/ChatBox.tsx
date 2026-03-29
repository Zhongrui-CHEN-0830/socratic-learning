import { useState, useRef, KeyboardEvent, FormEvent, RefObject } from 'react'
import type { Message } from '../pages/Dashboard'
import styles from './ChatBox.module.css'

interface Props {
  messages: Message[]
  loading: boolean
  onSendMessage: (text: string) => void
  messagesEndRef: RefObject<HTMLDivElement | null>
}

export default function ChatBox({ messages, loading, onSendMessage, messagesEndRef }: Props) {
  const [input, setInput] = useState('')
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  function handleSend() {
    const text = input.trim()
    if (!text || loading) return
    setInput('')
    autoResize()
    onSendMessage(text)
  }

  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  function autoResize() {
    const ta = textareaRef.current
    if (!ta) return
    ta.style.height = 'auto'
    ta.style.height = Math.min(ta.scrollHeight, 120) + 'px'
  }

  function renderMessageContent(content: string) {
    // Split by character markers 【慕千汐】or【桑稚】
    const parts = content.split(/(【慕千汐】|【桑稚】)/g)
    const elements: React.ReactElement[] = []

    parts.forEach((part, i) => {
      if (part === '【慕千汐】') {
        elements.push(
          <span key={i} className={`${styles.charName} ${styles.charMu}`}>
            <span className={styles.charDot} />
            慕千汐
          </span>
        )
      } else if (part === '【桑稚】') {
        elements.push(
          <span key={i} className={`${styles.charName} ${styles.charSang}`}>
            <span className={styles.charDot} />
            桑稚
          </span>
        )
      } else if (part.trim()) {
        // Process text: bold, italic, actions, code, math, newlines
        const processed = part
          .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
          .replace(/\*(.+?)\*/g, '<em>$1</em>')
          .replace(/（([^）]+)）/g, '<span class="action">（$1）</span>')
          .replace(/`([^`]+)`/g, '<code>$1</code>')
          .replace(/\n/g, '<br>')
        elements.push(
          <span key={i} className={styles.para} dangerouslySetInnerHTML={{ __html: processed }} />
        )
      }
    })

    return elements
  }

  if (messages.length === 0) {
    return (
      <div className={styles.empty}>
        <div className={styles.emptyInner}>
          <div className={styles.emptyAvatars}>
            <div className={`${styles.emptyAvatar} ${styles.mu}`}>千</div>
            <div className={`${styles.emptyAvatar} ${styles.sang}`}>稚</div>
          </div>
          <h2 className={styles.emptyTitle}>欢迎来到墨韵书院</h2>
          <p className={styles.emptyDesc}>请在左侧上传教材，然后开始与你的虚拟教师对话。<br/>他们会记住你的一切——你的进步，你的弱点，还有你在学习中流露的情感。</p>
        </div>
        <div className={styles.inputArea}>
          <TextArea input={input} setInput={setInput} textareaRef={textareaRef} onKeyDown={handleKeyDown} onSend={handleSend} loading={loading} />
        </div>
      </div>
    )
  }

  return (
    <div className={styles.chatBox}>
      <div className={styles.messages}>
        {messages.map(msg => (
          <div
            key={msg.id}
            className={`${styles.message} ${msg.role === 'user' ? styles.userMsg : styles.assistantMsg}`}
          >
            {msg.role === 'user' ? (
              <div className={styles.userBubble}>
                <p>{msg.content}</p>
              </div>
            ) : (
              <div className={styles.assistantBubble}>
                {msg.character === 'mu' && (
                  <div className={`${styles.charTag} ${styles.muTag}`}>千汐</div>
                )}
                {msg.character === 'sang' && (
                  <div className={`${styles.charTag} ${styles.sangTag}`}>桑稚</div>
                )}
                <div className={styles.content}>
                  {renderMessageContent(msg.content)}
                </div>
              </div>
            )}
          </div>
        ))}

        {loading && (
          <div className={`${styles.message} ${styles.assistantMsg}`}>
            <div className={styles.assistantBubble}>
              <div className={styles.loadingDots}>
                <span /><span /><span />
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <div className={styles.inputArea}>
        <TextArea input={input} setInput={setInput} textareaRef={textareaRef} onKeyDown={handleKeyDown} onSend={handleSend} loading={loading} />
      </div>
    </div>
  )
}

function TextArea({ input, setInput, textareaRef, onKeyDown, onSend, loading }: {
  input: string
  setInput: (v: string) => void
  textareaRef: RefObject<HTMLTextAreaElement | null>
  onKeyDown: (e: KeyboardEvent<HTMLTextAreaElement>) => void
  onSend: () => void
  loading: boolean
}) {
  return (
    <div className={styles.inputWrapper}>
      <textarea
        ref={textareaRef}
        className={styles.textarea}
        value={input}
        onChange={e => { setInput(e.target.value); autoResize(e.target) }}
        onKeyDown={onKeyDown}
        placeholder="输入消息...（Enter 发送，Shift+Enter 换行）"
        rows={1}
        disabled={loading}
      />
      <button
        className={styles.sendBtn}
        onClick={onSend}
        disabled={!input.trim() || loading}
        aria-label="发送"
      >
        <svg viewBox="0 0 20 20" fill="currentColor" width="18" height="18">
          <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z"/>
        </svg>
      </button>
    </div>
  )
}

function autoResize(el: HTMLTextAreaElement) {
  el.style.height = 'auto'
  el.style.height = Math.min(el.scrollHeight, 120) + 'px'
}
