#!/usr/bin/env node
// stdin: {records: kept records, date, kw_version} -> stdout: published state (shared/lib/delta.js nextState from an empty state)
const path = require('path');
const {slim, nextState, keyOf} = require(path.join(__dirname, '..', 'shared', 'lib', 'delta.js'));
let s = ''; process.stdin.on('data', d => s += d).on('end', () => {
  const i = JSON.parse(s); const kept = {};
  for (const r of i.records) kept[keyOf(r)] = slim(r);
  const sources = {}; for (const r of i.records) sources[r.company] = {status: 'ok'};
  process.stdout.write(JSON.stringify(nextState({}, {date: i.date, kw_version: i.kw_version, kept, all: {}, sources})));
});
