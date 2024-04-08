#!/usr/bin/node
const { argv } = require('node:process');

if (!argv[2] || !argv[3]) {
  console.log(NaN);
} else {
  add(argv[2], argv[3]);
}
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  console.log(a + b);
}
