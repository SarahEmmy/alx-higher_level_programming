#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.w = width;
      this.h = height;
    }
  }

  print () {
    let j = 0;
    for (j; j < this.h; j++) {
      console.log('X'.repeat(this.w));
    }
  }
}
module.exports = Rectangle;
