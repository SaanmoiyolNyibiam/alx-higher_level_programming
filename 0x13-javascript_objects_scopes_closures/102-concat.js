#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');

const dataA = fs.readFileSync(argv[2], 'utf8');
const dataB = fs.readFileSync(argv[3], 'utf8');
fs.writeFileSync(argv[4], dataA, 'utf8');
fs.appendFileSync(argv[4], dataB, 'utf8');
