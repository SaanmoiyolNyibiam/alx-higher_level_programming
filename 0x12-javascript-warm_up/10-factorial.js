#!/usr/bin/node
const { argv } = require('node:process');

if (!argv[2]) {
  console.log(1);
} else {
  console.log(factorial(argv[2]));
}
function factorial (a) {
  a = parseInt(a);
  if (a === 0) { return (1); }
  return (a * factorial(a - 1));
}
