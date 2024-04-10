#!/usr/bin/node

exports.esrever = function (list) {
  const actualLen = list.length - 1;
  const len = list.length % 2 ? (list.length / 2) - 0.5 : list.length / 2;
  let index = 0;
  let temp;
  while (index < len) {
    temp = list[actualLen - index];
    list[actualLen - index] = list[index];
    list[index] = temp;
    index++;
  }
  return (list);
};
