import {
  readTeacherFile,
  writeTeacherFile,
  appendTeacherFile,
  getLineCount,
} from './files.js';
import { generateSettlement, clearHistory } from './chat.js';

export async function endSession(): Promise<string> {
  const result = await generateSettlement();

  const today = new Date().toLocaleDateString('zh-CN');

  // 1. Update diary
  if (result.diary) {
    await appendTeacherFile('diary.md', `\n## ${today}\n\n${result.diary}\n\n---`);
  }

  // 2. Update progress
  if (result.progress) {
    await appendTeacherFile('progress.md', `\n## ${today}\n\n${result.progress}`);
  }

  // 3. Check if progress.md is too long, archive old content
  const lineCount = await getLineCount('progress.md');
  if (lineCount > 200) {
    const content = await readTeacherFile('progress.md');
    const lines = content.split('\n');
    const keepLines = lines.slice(-100);
    const archiveLines = lines.slice(0, lines.length - 100);

    await writeTeacherFile('progress.md', `# 学习进度\n\n${keepLines.join('\n')}`);
    await appendTeacherFile('archive.md', `\n## 存档于 ${today}\n\n${archiveLines.join('\n')}\n\n---`);
  }

  // 4. Update textbook notes
  if (result.textbookNotes) {
    await appendTeacherFile('textbook-notes.md', `\n## ${today}\n\n${result.textbookNotes}`);
  }

  // 5. Update character profiles
  if (result.muUpdate) {
    const muContent = await readTeacherFile('mu-qianxi.md');
    const updated = muContent.replace(
      /(\*\*当前状态：).*$/m,
      `$1${today} 更新**\n\n${result.muUpdate}`
    );
    await writeTeacherFile('mu-qianxi.md', updated);
  }

  if (result.sangUpdate) {
    const sangContent = await readTeacherFile('sang-zhi.md');
    const updated = sangContent.replace(
      /(\*\*当前状态：).*$/m,
      `$1${today} 更新**\n\n${result.sangUpdate}`
    );
    await writeTeacherFile('sang-zhi.md', updated);
  }

  // 6. Clear conversation history for next session
  clearHistory();

  return result.farewell;
}
