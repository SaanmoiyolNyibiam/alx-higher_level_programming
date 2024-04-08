#!/usr/bin/node
const { argv } = require('node:process');

const input = parseInt(argv[2]);
if (isNaN(input)) {
  console.log('Missing size');
} else {
  const times = argv[2];
  let height = 0;
  let width = 0;
  let output = '';
  while (height < times) {
    while (width < times) {
      output += 'X';
      width++;
    }
    console.log(output);
    height++;
  }
}
