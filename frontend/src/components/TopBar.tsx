import { useNavigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'
import styles from './TopBar.module.css'

interface Props {
  onToggleSidebar: () => void
  sidebarOpen: boolean
}

export default function TopBar({ onToggleSidebar, sidebarOpen }: Props) {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  return (
    <header className={styles.topbar}>
      {/* Left: menu toggle + title */}
      <div className={styles.left}>
        <button className={styles.menuBtn} onClick={onToggleSidebar} aria-label="切换侧边栏">
          <svg viewBox="0 0 20 20" fill="currentColor" width="20" height="20">
            {sidebarOpen ? (
              <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd"/>
            ) : (
              <path fillRule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clipRule="evenodd"/>
            )}
          </svg>
        </button>
        <div className={styles.title}>
          <span className={styles.titleMain}>墨韵书院</span>
          <span className={styles.titleSep}>·</span>
          <span className={styles.titleSub}>苏格拉底伴学</span>
        </div>
      </div>

      {/* Right: user menu */}
      <div className={styles.right}>
        <div className={styles.userMenu}>
          <div className={styles.avatar}>
            {user?.email?.[0]?.toUpperCase() || 'U'}
          </div>
          <div className={styles.userInfo}>
            <span className={styles.userEmail}>{user?.email}</span>
          </div>
          <button
            className={styles.logoutBtn}
            onClick={() => { logout(); navigate('/login') }}
            title="退出登录"
          >
            <svg viewBox="0 0 20 20" fill="currentColor" width="16" height="16">
              <path fillRule="evenodd" d="M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z" clipRule="evenodd"/>
            </svg>
          </button>
        </div>
      </div>
    </header>
  )
}
