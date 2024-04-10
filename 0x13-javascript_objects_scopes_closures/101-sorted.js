#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  newDict[dict[key]] = [];
}
for (const key1 in newDict) {
  for (const key2 in dict) {
    if (+dict[key2] === +key1) {
      newDict[key1].push(key2);
    }
  }
}
console.log(newDict);
