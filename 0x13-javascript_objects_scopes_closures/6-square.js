#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
