// Port of lectern/collect.py: plain(), iso_date(), normalise(). Pure functions: no n8n globals.
const NAMED = {amp:'&', lt:'<', gt:'>', quot:'"', apos:"'", nbsp:' ', ndash:'–', mdash:'—',
  lsquo:'‘', rsquo:'’', ldquo:'“', rdquo:'”', hellip:'…', bull:'•', middot:'·',
  copy:'©', reg:'®', trade:'™', eacute:'é', egrave:'è', aacute:'á', agrave:'à',
  uuml:'ü', ouml:'ö', auml:'ä', ntilde:'ñ', ccedil:'ç', deg:'°', times:'×',
  euro:'€', pound:'£', laquo:'«', raquo:'»', iexcl:'¡', iquest:'¿', szlig:'ß'};
const CP1252 = {0x80:0x20ac,0x82:0x201a,0x83:0x0192,0x84:0x201e,0x85:0x2026,0x86:0x2020,0x87:0x2021,0x88:0x02c6,
  0x89:0x2030,0x8a:0x0160,0x8b:0x2039,0x8c:0x0152,0x8e:0x017d,0x91:0x2018,0x92:0x2019,0x93:0x201c,0x94:0x201d,
  0x95:0x2022,0x96:0x2013,0x97:0x2014,0x98:0x02dc,0x99:0x2122,0x9a:0x0161,0x9b:0x203a,0x9c:0x0153,0x9e:0x017e,0x9f:0x0178};

function unescapeHtml(s) {
  return s.replace(/&(#[xX][0-9a-fA-F]+|#[0-9]+|[A-Za-z][A-Za-z0-9]*);/g, (m, e) => {
    if (e[0] === '#') {
      let cp = (e[1] === 'x' || e[1] === 'X') ? parseInt(e.slice(2), 16) : parseInt(e.slice(1), 10);
      if (cp === 0 || cp > 0x10ffff || (cp >= 0xd800 && cp <= 0xdfff)) return '�';
      if (CP1252[cp]) cp = CP1252[cp];
      return String.fromCodePoint(cp);
    }
    return Object.prototype.hasOwnProperty.call(NAMED, e) ? NAMED[e] : m;
  });
}

// Python: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(html.unescape(s or "")))).strip()
function plain(s) {
  return unescapeHtml(unescapeHtml(s || '')).replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
}

function isoDate(v) {
  if (!v) return null;
  const m = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(v));
  return m ? m[0] : null;
}

const pystr = v => (v === undefined || v === null) ? 'None' : String(v);   // Python str(None) is 'None'
const joinTruthy = (xs, sep) => xs.filter(x => x).join(sep);

function normalise(provider, company, payload) {
  const out = [];
  for (const j of (payload && payload.jobs) || []) {
    let v;
    if (provider === 'greenhouse') {
      v = {source_id: pystr(j.id), title: (j.title || '').trim(), text: plain(j.content),
           location_text: (j.location || {}).name || '', date_raw: j.first_published || j.updated_at || null,
           url: j.absolute_url === undefined ? null : j.absolute_url,
           department: (j.departments || []).map(d => d.name || '').join(' / '),
           job_ref: (j.internal_job_id !== undefined && j.internal_job_id !== null) ? String(j.internal_job_id) : null};
    } else if (provider === 'ashby') {
      const locs = [j.location || ''].concat((j.secondaryLocations || []).map(x => x.location || ''));
      v = {source_id: pystr(j.id), title: (j.title || '').trim(), text: plain(j.descriptionHtml || j.descriptionPlain),
           location_text: joinTruthy(locs, ' · '), date_raw: j.publishedAt || null,
           url: j.jobUrl === undefined ? null : j.jobUrl, department: joinTruthy([j.department, j.team], ' / ')};
    } else {   // smartrecruiters
      const secs = ((j.jobAd || {}).sections || {});
      const cf = {};
      for (const f of (j.customField || [])) cf[f.fieldLabel] = f.valueLabel;
      const loc = j.location || {};
      v = {source_id: pystr(j.id), title: (j.name || '').trim(),
           text: plain(Object.values(secs).map(x => ((x || {}).text) || '').join(' ')),
           location_text: loc.fullLocation || '', date_raw: j.releasedDate || null,
           url: j.postingUrl === undefined ? null : j.postingUrl,
           department: joinTruthy([(j.function || {}).label, cf.Org], ' / ')};
    }
    if (v.job_ref === undefined) v.job_ref = null;
    Object.assign(v, {source: provider, company, date_posted: isoDate(v.date_raw), original: j});
    out.push(v);
  }
  return out;
}
if (typeof module !== 'undefined') module.exports = {plain, isoDate, normalise, unescapeHtml};
