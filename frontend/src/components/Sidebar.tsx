import { useRef } from 'react'
import type { Conversation, Textbook } from '../pages/Dashboard'
import styles from './Sidebar.module.css'

interface Props {
  open: boolean
  conversations: Conversation[]
  activeConversationId: string | null
  textbooks: Textbook[]
  currentTextbook: string | null
  onSelectConversation: (id: string) => void
  onNewConversation: () => void
  onDeleteConversation: (id: string) => void
  onSelectTextbook: (id: string) => void
  onUploadTextbook: (file: File) => void
  onDeleteTextbook: (id: string) => void
  onEndSession: () => void
  onToggle: () => void
}

export default function Sidebar({
  open,
  conversations,
  activeConversationId,
  textbooks,
  currentTextbook,
  onSelectConversation,
  onNewConversation,
  onDeleteConversation,
  onSelectTextbook,
  onUploadTextbook,
  onDeleteTextbook,
  onEndSession,
  onToggle,
}: Props) {
  const uploadRef = useRef<HTMLInputElement>(null)

  function handleFileChange(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0]
    if (file) {
      onUploadTextbook(file)
      e.target.value = ''
    }
  }

  return (
    <>
      {/* Mobile overlay */}
      {open && <div className={styles.overlay} onClick={onToggle} />}

      <aside className={`${styles.sidebar} ${open ? styles.open : ''}`}>
        {/* Header */}
        <div className={styles.header}>
          <div className={styles.logo}>
            <svg viewBox="0 0 32 32" width="28" height="28">
              <rect width="32" height="32" rx="7" fill="var(--ink-surface-2)"/>
              <text x="16" y="22" textAnchor="middle" fontSize="17" fontFamily="serif" fill="var(--gold-accent)">墨</text>
            </svg>
            <span className={styles.logoText}>墨韵书院</span>
          </div>
          <button className={styles.closeBtn} onClick={onToggle} aria-label="关闭侧边栏">
            <svg viewBox="0 0 20 20" fill="currentColor" width="18" height="18">
              <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd"/>
            </svg>
          </button>
        </div>

        {/* Sections */}
        <div className={styles.content}>
          {/* Textbooks */}
          <section className={styles.section}>
            <div className={styles.sectionHeader}>
              <h3>教材</h3>
            </div>
            <div className={styles.textbookList}>
              {textbooks.map(tb => (
                <div
                  key={tb.id}
                  className={`${styles.textbookItem} ${tb.id === currentTextbook ? styles.active : ''}`}
                  onClick={() => onSelectTextbook(tb.id)}
                  title={tb.filename}
                >
                  <svg viewBox="0 0 20 20" fill="currentColor" width="14" height="14" className={styles.textbookIcon}>
                    <path fillRule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clipRule="evenodd"/>
                  </svg>
                  <span className={styles.textbookName}>{tb.filename.replace('.md', '')}</span>
                  <button
                    className={styles.deleteBtn}
                    onClick={e => { e.stopPropagation(); onDeleteTextbook(tb.id) }}
                    title="删除"
                  >
                    ×
                  </button>
                </div>
              ))}
              {textbooks.length === 0 && (
                <p className={styles.empty}>暂无教材</p>
              )}
            </div>
            <label className={styles.uploadBtn}>
              <svg viewBox="0 0 20 20" fill="currentColor" width="14" height="14">
                <path fillRule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM6.293 6.707a1 1 0 010-1.414l3-3a1 1 0 011.414 0l3 3a1 1 0 01-1.414 1.414L11 5.414V13a1 1 0 11-2 0V5.414L7.707 6.707a1 1 0 01-1.414 0z" clipRule="evenodd"/>
              </svg>
              上传教材 (.md)
              <input ref={uploadRef} type="file" accept=".md" onChange={handleFileChange} hidden />
            </label>
          </section>

          {/* Tools */}
          <section className={styles.section}>
            <div className={styles.sectionHeader}>
              <h3>工具</h3>
            </div>
            <div className={styles.toolList}>
              <button className={`${styles.toolBtn} ${styles.endBtn}`} onClick={onEndSession}>
                <svg viewBox="0 0 20 20" fill="currentColor" width="15" height="15">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8 7a1 1 0 00-1 1v4a1 1 0 001 1h4a1 1 0 001-1V8a1 1 0 00-1-1H8z" clipRule="evenodd"/>
                </svg>
                结束当天学习
              </button>
              <button className={styles.toolBtn} onClick={() => window.open('/app/settings', '_self')}>
                <svg viewBox="0 0 20 20" fill="currentColor" width="15" height="15">
                  <path fillRule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clipRule="evenodd"/>
                </svg>
                API 设置
              </button>
            </div>
          </section>

          {/* Conversations */}
          <section className={`${styles.section} ${styles.conversationsSection}`}>
            <div className={styles.sectionHeader}>
              <h3>对话历史</h3>
              <button className={styles.newBtn} onClick={onNewConversation} title="新建对话">
                <svg viewBox="0 0 20 20" fill="currentColor" width="16" height="16">
                  <path fillRule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clipRule="evenodd"/>
                </svg>
              </button>
            </div>
            <div className={styles.convList}>
              {conversations.map(conv => (
                <div
                  key={conv.id}
                  className={`${styles.convItem} ${conv.id === activeConversationId ? styles.active : ''}`}
                  onClick={() => onSelectConversation(conv.id)}
                >
                  <span className={styles.convTitle}>{conv.title || '新对话'}</span>
                  <button
                    className={styles.deleteBtn}
                    onClick={e => { e.stopPropagation(); onDeleteConversation(conv.id) }}
                    title="删除"
                  >
                    ×
                  </button>
                </div>
              ))}
              {conversations.length === 0 && (
                <p className={styles.empty}>暂无对话记录</p>
              )}
            </div>
          </section>
        </div>
      </aside>
    </>
  )
}
