#!/usr/bin/env node
// stdin: {new, watched, first_time, already}  ->  stdout: {rows:[keys], messages:[...]}  using shared/lib/messages.js
const path = require('path');
const {buildMessages} = require(path.join(__dirname, '..', 'shared', 'lib', 'messages.js'));
let s = ''; process.stdin.on('data', d => s += d).on('end', () => {
  const i = JSON.parse(s); const r = buildMessages(i.new, i.watched, i.first_time, i.already);
  process.stdout.write(JSON.stringify({rows: r.rows.map(x => `${x.source}:${x.source_id}`), messages: r.messages}));
});
