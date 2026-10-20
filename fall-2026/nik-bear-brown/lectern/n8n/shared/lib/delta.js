// Port of lectern/publish_delta.py: norm_matched(), slim(), fingerprint(), diff(), write_state().
// Pure functions: no n8n globals. Hashes use a small non-cryptographic function (the Code node has no crypto
// module by default), so a state file written here is not interchangeable with the Python one.
const FIELDS = ['title', 'url', 'location_text', 'department'];

function hash(s) {   // cyrb53, hex
  let h1 = 0xdeadbeef, h2 = 0x41c6ce57;
  for (let i = 0; i < s.length; i++) {
    const ch = s.charCodeAt(i);
    h1 = Math.imul(h1 ^ ch, 2654435761); h2 = Math.imul(h2 ^ ch, 1597334677);
  }
  h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
  h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
  return (4294967296 * (2097151 & h2) + (h1 >>> 0)).toString(16).padStart(14, '0');
}
function stable(x) {   // JSON with sorted keys at every level
  if (Array.isArray(x)) return '[' + x.map(stable).join(',') + ']';
  if (x && typeof x === 'object') return '{' + Object.keys(x).sort().map(k => JSON.stringify(k) + ':' + stable(x[k])).join(',') + '}';
  return JSON.stringify(x === undefined ? null : x);
}
const keyOf = r => `${r.source}:${r.source_id}`;
const isEmpty = v => v === null || v === undefined || v === false || v === 0 ||
  (Array.isArray(v) && v.length === 0) || (v && typeof v === 'object' && !Array.isArray(v) && Object.keys(v).length === 0);

// Drop empty entries so a rule added to the filter is not reported as a change to every posting.
function normMatched(m) {
  if (!m || typeof m !== 'object' || Array.isArray(m)) return m === undefined ? null : m;
  const out = {};
  for (const k of Object.keys(m)) if (!isEmpty(m[k])) out[k] = m[k];
  return out;
}
function slim(r) {
  const out = {};
  for (const k of ['company', 'source', 'source_id', ...FIELDS, 'date_posted']) out[k] = r[k] === undefined ? null : r[k];
  out.matched = normMatched(r.matched);
  out.text_sha = (r.text !== undefined && r.text !== null) ? hash(r.text) : null;
  return out;
}
function fingerprint(s) {
  const o = {};
  for (const k of [...FIELDS, 'matched', 'text_sha']) o[k] = s[k] === undefined ? null : s[k];
  return hash(stable(o));
}

// run = {date, kw_version, kept: {key: slim}, all: {key: record}, sources: {company: status}}
function diff(stateC, run) {
  const nw = [], changed = [], gone = [];
  for (const [k, s] of Object.entries(run.kept)) {
    if (!(k in stateC)) { nw.push(s); continue; }
    const old = stateC[k];
    if (fingerprint(s) !== old.fp) {
      const what = [];
      for (const f of [...FIELDS, 'matched', 'text_sha']) {
        if (stable(s[f] === undefined ? null : s[f]) !== stable(old[f] === undefined ? null : old[f]))
          what.push({field: f === 'text_sha' ? 'ad text' : f, before: f === 'text_sha' ? null : (old[f] === undefined ? null : old[f]),
                     after: f === 'text_sha' ? null : (s[f] === undefined ? null : s[f])});
      }
      changed.push(Object.assign({}, s, {changes: what}));
    }
  }
  for (const [k, old] of Object.entries(stateC)) {
    if (k in run.kept) continue;
    const src = run.sources[old.company];
    let why;
    if (src === undefined) why = 'company not watched in this run';
    else if (src.status !== 'ok') why = `unknown: source ${src.status} today (${src.reason === undefined ? 'no reason given' : src.reason})`;
    else if (k in run.all) why = 'still on the board, no longer kept by the filter: ' + String(run.all[k].reject_reason === undefined ? 'None' : run.all[k].reject_reason);
    else why = 'no longer on the board';
    gone.push(Object.assign({}, old, {why}));
  }
  const baseCos = new Set(Object.values(stateC).map(v => v.company));
  const firstTime = [...new Set(nw.filter(r => !baseCos.has(r.company)).map(r => r.company))].sort();
  return {new: nw, changed, gone, first_time_companies: firstTime};
}

// The published state after this run: kept rows are written, and a gone row is dropped only if its source was readable.
function nextState(stateC, run) {
  const c = Object.assign({}, stateC);
  for (const [k, v] of Object.entries(run.kept)) {
    const prev = c[k];
    c[k] = Object.assign({}, v, {fp: fingerprint(v), published: prev ? prev.published : run.date, last_published: run.date});
  }
  for (const k of Object.keys(c)) {
    const src = run.sources[c[k].company];
    if (!(k in run.kept) && src && src.status === 'ok') delete c[k];
  }
  return {schema: 1, as_of: run.date, kw_version: run.kw_version, candidates: c};
}
if (typeof module !== 'undefined') module.exports = {slim, fingerprint, diff, nextState, normMatched, hash, stable, keyOf};
