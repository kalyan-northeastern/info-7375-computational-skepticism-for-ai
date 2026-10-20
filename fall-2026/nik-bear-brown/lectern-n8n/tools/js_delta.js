#!/usr/bin/env node
// Runs shared/lib/delta.js: state from an earlier run's kept set, diff against a later run. Prints JSON.
// usage: node tools/js_delta.js <earlier-kept.json> <earlier-all.json> <later-kept.json> <later-all.json> <later-date>
const fs = require('fs'), path = require('path');
const {slim, diff, nextState, keyOf} = require(path.join(__dirname, '..', 'shared', 'lib', 'delta.js'));
const load = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const [ek, ea, lk, la, date] = process.argv.slice(2);
function runOf(keptP, allP, d) {
  const kept = load(keptP), all = load(allP);
  const k = {}, a = {};
  for (const r of kept.records) k[keyOf(r)] = slim(r);
  for (const r of all.records) a[keyOf(r)] = r;
  const sources = {}; for (const s of (all.sources || kept.sources || [])) sources[s.company] = s;
  return {date: d, kw_version: all.keywords_version || null, kept: k, all: a, sources};
}
const early = runOf(ek, ea, 'earlier'), later = runOf(lk, la, date);
const state = nextState({}, early).candidates;
const out = diff(state, later);
const sum = r => ({key: keyOf(r), why: r.why || null, fields: (r.changes || []).map(c => c.field)});
process.stdout.write(JSON.stringify({new: out.new.map(sum), changed: out.changed.map(sum), gone: out.gone.map(sum), first_time: out.first_time_companies}));
