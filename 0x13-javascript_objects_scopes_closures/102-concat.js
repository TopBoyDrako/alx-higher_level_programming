#!/usr/bin/node

const fileSource = require('fileSource');
const a = fileSource.readFileSync(process.argv[2], 'utf8');
const b = fileSource.readFileSync(process.argv[3], 'utf8');
fileSource.writeFileSync(process.argv[4], a + b);
