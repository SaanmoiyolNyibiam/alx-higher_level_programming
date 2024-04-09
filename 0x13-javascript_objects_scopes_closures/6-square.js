#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (printChar) {
    if (printChar) {
      this.printChar = printChar;
      this.print();
    } else {
      this.print();
    }
  }
}

module.exports = Square;
