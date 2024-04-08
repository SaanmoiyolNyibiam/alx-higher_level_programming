#!/usr/bin/node
const { argv } = require('node:process');

const input = parseInt(argv[2]);
if (input) {
  console.log('My number:', input);
} else {
  console.log('Not a number');
}
