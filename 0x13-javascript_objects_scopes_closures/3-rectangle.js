#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let width = 0;
    let height = 0;
    let output = '';
    while (height < this.height) {
      while (width < this.width) {
        output += 'X';
        width++;
      }
      console.log(output);
      height++;
    }
  }
}

module.exports = Rectangle;
