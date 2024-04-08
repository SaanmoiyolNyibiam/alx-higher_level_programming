#!/usr/bin/node
const { argv } = require('node:process');

const input = parseInt(argv[2]);
if (isNaN(input)) {
  console.log('Missing number of occurrences');
} else {
  const times = argv[2];
  let index = 0;
  while (index < times) {
    console.log('C is fun');
    index++;
  }
}
