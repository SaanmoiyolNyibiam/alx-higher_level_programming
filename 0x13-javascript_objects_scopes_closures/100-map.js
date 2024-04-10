#!/usr/bin/node
const array = require('./100-data').list;

const arrayCopy = array.map((x, index) => x * index);
console.log(array);
console.log(arrayCopy);
