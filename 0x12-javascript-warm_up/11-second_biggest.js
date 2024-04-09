#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 4) {
  console.log(0);
} else {
  const intArray = [];
  let i = 2;
  while (argv[i]) {
    intArray.push(parseInt(argv[i]));
    i++;
  }
  intArray.sort((a, b) => b - a);
  console.log(intArray[1]);
}
