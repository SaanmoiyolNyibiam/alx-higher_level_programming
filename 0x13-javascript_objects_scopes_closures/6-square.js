#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (printChar) {
    if (printChar) {
      let width = 0;
      let height = 0;
      let output = '';
      while (height < this.height) {
        while (width < this.width) {
          output += printChar;
          width++;
        }
        console.log(output);
        height++;
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
