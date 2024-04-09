#!/usr/bin/node

function callMeMoby (x, theFunction) {
  let index = 0;
  while (index < x) {
    theFunction();
    index++;
  }
}

module.exports.callMeMoby = callMeMoby;
