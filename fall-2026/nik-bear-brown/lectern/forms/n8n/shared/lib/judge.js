// Port of lectern/collect.py: word_in(), materials_evidence(), connector_evidence(), judge(), and the
// dedupe and validity checks from main(). Pure functions: no n8n globals. The rules are keywords.json, never this file.
const escRe = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
function wordIn(word, text) {
  return new RegExp('(?<![a-z0-9])' + escRe(word.toLowerCase()) + '(?![a-z0-9])').test(text);
}

function materialsEvidence(bodyLc, kw) {
  const rule = kw.materials_rule || {};
  if (!Object.keys(rule).length) return null;
  const vo = (rule.verb_object || []).filter(p => bodyLc.includes(p.toLowerCase()));
  const au = (rule.audience || []).filter(p => bodyLc.includes(p.toLowerCase()));
  const minVo = rule.min_verb_object === undefined ? 1 : rule.min_verb_object;
  const minAu = rule.min_audience === undefined ? 1 : rule.min_audience;
  if (vo.length >= minVo && au.length >= minAu) return {verb_object: vo.slice(0, 6), audience: au.slice(0, 6)};
  return null;
}

function connectorEvidence(titleLc, bodyLc, kw) {
  const rule = kw.connector_rule || {};
  if (!Object.keys(rule).length) return null;
  const tw = (rule.title_words || []).filter(w => wordIn(w, titleLc));
  const iw = (rule.institution_words || []).filter(w => wordIn(w, bodyLc));
  return (tw.length && iw.length) ? {title: tw, institution: iw.slice(0, 6)} : null;
}

// Returns [matched, rejectReason]; exactly one is null.
function judge(v, kw) {
  const ignore = new Set(((kw.ignore_words_by_company || {})[v.company] || []).map(w => w.toLowerCase()));
  const tl = v.title.toLowerCase(), bl = v.text.toLowerCase();
  const role = kw.role_title.filter(w => !ignore.has(w.toLowerCase()) && wordIn(w, tl));
  const topic = kw.topic_text.filter(w => !ignore.has(w.toLowerCase()) && wordIn(w, bl));
  const flex = kw.flex_text.filter(w => wordIn(w, bl));
  const need = kw.keep_rule.topic_text_min_if_no_title_match;
  const mats = materialsEvidence(bl, kw);
  const conn = connectorEvidence(tl, bl, kw);
  let why;
  if (role.length) why = 'role word in title';
  else if (topic.length >= need) why = `${topic.length} topic words in body (>= ${need})`;
  else if (mats) why = 'body says it produces teaching materials for a named audience';
  else if (conn) why = 'account or partnership role whose body names higher education';
  else return [null, (!(role.length || topic.length) ? 'no-keyword-match' : `only ${topic.length} topic words, no role word in title`)];
  return [{role_title: role, topic_text: topic, flex_text: flex, materials: mats, connector: conn,
           kept_because: why, title_only: Boolean(role.length && !topic.length)}, null];
}

// The per-posting checks in collect.main(): returns a reject reason, or null if the posting goes on to judge().
function validity(v) {
  if (!v.title) return 'missing-title';
  if (!v.url) return 'missing-url';
  if (!v.date_posted) return 'unparseable-date';
  return null;
}
if (typeof module !== 'undefined') module.exports = {wordIn, judge, validity, materialsEvidence, connectorEvidence};
