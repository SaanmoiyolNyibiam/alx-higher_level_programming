#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let index = 0;
  let count = 0;
  while (list[index]) {
    if (searchElement === list[index]) {
      count++;
      index++;
      continue;
    }
    index++;
  }
  return count;
};
