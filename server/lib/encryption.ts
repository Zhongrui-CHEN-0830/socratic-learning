import crypto from 'crypto'

const ALGORITHM = 'aes-256-gcm'
const KEY_LENGTH = 32
const IV_LENGTH = 12
const AUTH_TAG_LENGTH = 16

function getKey(): Buffer {
  const key = process.env.ENCRYPTION_KEY
  if (!key) throw new Error('ENCRYPTION_KEY env var is required')
  // Derive a 32-byte key from the env var using SHA-256
  return crypto.createHash('sha256').update(key).digest()
}

export function encrypt(plaintext: string): { encrypted: string; iv: string } {
  const iv = crypto.randomBytes(IV_LENGTH)
  const cipher = crypto.createCipheriv(ALGORITHM, getKey(), iv, {
    authTagLength: AUTH_TAG_LENGTH,
  })

  let encrypted = cipher.update(plaintext, 'utf8', 'hex')
  encrypted += cipher.final('hex')
  const authTag = cipher.getAuthTag()

  // Combine encrypted + authTag
  const combined = encrypted + authTag.toString('hex')
  return {
    encrypted: combined,
    iv: iv.toString('hex'),
  }
}

export function decrypt(encrypted: string, ivHex: string): string {
  const iv = Buffer.from(ivHex, 'hex')
  const authTagHex = encrypted.slice(-AUTH_TAG_LENGTH * 2)
  const encryptedText = encrypted.slice(0, -AUTH_TAG_LENGTH * 2)

  const decipher = crypto.createDecipheriv(ALGORITHM, getKey(), iv, {
    authTagLength: AUTH_TAG_LENGTH,
  })
  decipher.setAuthTag(Buffer.from(authTagHex, 'hex'))

  let decrypted = decipher.update(encryptedText, 'hex', 'utf8')
  decrypted += decipher.final('utf8')
  return decrypted
}

export function maskKey(key: string): string {
  if (key.length <= 8) return '***'
  return key.slice(0, 6) + '***' + key.slice(-4)
}
