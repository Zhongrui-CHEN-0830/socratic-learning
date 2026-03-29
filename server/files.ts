import { promises as fs } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = path.join(__dirname, '..');
const TEACHER_DIR = path.join(PROJECT_ROOT, 'teacher');
const TEXTBOOKS_DIR = path.join(PROJECT_ROOT, 'textbooks');

export async function readTeacherFile(filename: string): Promise<string> {
  const filepath = path.join(TEACHER_DIR, filename);
  try {
    return await fs.readFile(filepath, 'utf-8');
  } catch {
    return '';
  }
}

export async function writeTeacherFile(filename: string, content: string): Promise<void> {
  const filepath = path.join(TEACHER_DIR, filename);
  await fs.writeFile(filepath, content, 'utf-8');
}

export async function appendTeacherFile(filename: string, content: string): Promise<void> {
  const filepath = path.join(TEACHER_DIR, filename);
  const existing = await readTeacherFile(filename);
  await fs.writeFile(filepath, existing + '\n' + content, 'utf-8');
}

export async function listTextbooks(): Promise<string[]> {
  try {
    const files = await fs.readdir(TEXTBOOKS_DIR);
    return files.filter(f => f.endsWith('.md'));
  } catch {
    return [];
  }
}

export async function readTextbook(filename: string): Promise<string> {
  const filepath = path.join(TEXTBOOKS_DIR, filename);
  try {
    return await fs.readFile(filepath, 'utf-8');
  } catch {
    return '';
  }
}

export async function getLineCount(filename: string): Promise<number> {
  const content = await readTeacherFile(filename);
  return content.split('\n').length;
}
