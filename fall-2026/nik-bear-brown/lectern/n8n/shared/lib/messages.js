// Port of lectern/notify.py: matched_words(), order(), build_messages() and the refusal rule in post().
// Pure functions: no n8n globals. Nothing here can send anything; the Discord node does that, behind a switch.
const PRIORITY = ['Anthropic', 'OpenAI', 'Microsoft', 'Google', 'Figma', 'Canva', 'GitHub', 'Notion'];
const MAX_CHUNK = 1300;
const FOOTER = 'Every row links to the live posting. A person decides; the machine only ranks words.';
const REFUSE = /\/Users\/|\/home\/\w+|[\w.+-]+@[\w-]+\.[\w.]+|discord(app)?\.com\/api\/webhooks/;

function matchedWords(m) {
  if (!m || typeof m !== 'object' || Array.isArray(m)) return '';
  const words = [];
  for (const v0 of Object.values(m)) {
    let v = v0;
    if (v && typeof v === 'object' && !Array.isArray(v)) v = Object.values(v).filter(Array.isArray).flat();
    if (Array.isArray(v)) for (const w of v) if (!words.includes(w)) words.push(w);
  }
  return words.slice(0, 4).join(', ');
}
function order(rows) {
  const rank = {}; PRIORITY.forEach((c, i) => { rank[c] = i; });
  const r = c => (c in rank ? rank[c] : 99);
  const cmp = (a, b) => (a < b ? -1 : a > b ? 1 : 0);
  return rows.slice().sort((a, b) => (r(a.company) - r(b.company)) || cmp(a.company, b.company) || cmp(a.title || '', b.title || ''));
}
// Returns {rows, messages}. Drops unwatched companies and rows already posted.
function buildMessages(nw, watched, firstTime, already) {
  const W = new Set(watched), F = new Set(firstTime || []), A = new Set(already || []);
  let rows = nw.filter(r => W.has(r.company) && !A.has(`${r.source}:${r.source_id}`));
  rows = order(rows);
  if (!rows.length) return {rows: [], messages: []};
  const lines = rows.map(r => {
    const loc = (r.location_text || '').split(' | ')[0].split(';')[0].slice(0, 40);
    const tag = F.has(r.company) ? ' (newly watched)' : '';
    const mw = matchedWords(r.matched);
    return `**${r.company}**${tag}: ${(r.title || '').slice(0, 100)}` + (loc ? ` · ${loc}` : '') + (mw ? ` (${mw})` : '') + ` ${r.url || ''}`;
  });
  const msgs = []; let chunk = [], size = 0;
  for (const ln of lines) {
    if (size + ln.length > MAX_CHUNK && chunk.length) { msgs.push(chunk.join('\n')); chunk = []; size = 0; }
    chunk.push(ln); size += ln.length + 1;
  }
  if (chunk.length) msgs.push(chunk.join('\n'));
  msgs[msgs.length - 1] += '\n\n' + FOOTER;
  return {rows, messages: msgs};
}
const refused = text => REFUSE.test(text);
if (typeof module !== 'undefined') module.exports = {buildMessages, matchedWords, order, refused, PRIORITY, MAX_CHUNK, FOOTER};
