#!/usr/bin/env node
// Runs the JavaScript ports (shared/lib) over raw board payloads, the way workflows 01 and 02 do, and prints JSON.
// usage: node tools/js_run.js <keywords.json> <spec.json>   where spec = [{provider, company, file}]
const fs = require('fs'), path = require('path');
const lib = d => require(path.join(__dirname, '..', 'shared', 'lib', d));
const {normalise} = lib('normalise.js'), {judge, validity} = lib('judge.js');
const kw = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const spec = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const views = [];
for (const s of spec) views.push(...normalise(s.provider, s.company, JSON.parse(fs.readFileSync(s.file, 'utf8'))));
const seen = new Set(), recs = [], rejects = {};
for (const v of views) {
  const key = v.source + '\u0000' + v.source_id;
  if (seen.has(key)) { rejects.duplicate = (rejects.duplicate || 0) + 1; continue; }
  seen.add(key);
  let reason = validity(v), matched = null;
  if (!reason) { const [m, why] = judge(v, kw); if (m) matched = m; else reason = why; }
  if (reason) rejects[reason] = (rejects[reason] || 0) + 1;
  recs.push({source: v.source, company: v.company, source_id: v.source_id, title: v.title, text: v.text,
             location_text: v.location_text, department: v.department, date_posted: v.date_posted, job_ref: v.job_ref,
             url: v.url, kept: Boolean(matched), matched, reject_reason: reason});
}
process.stdout.write(JSON.stringify({fetched: views.length, records: recs, rejects}));
