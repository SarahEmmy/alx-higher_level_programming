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
    for (j; j< this.h; j++) {
      console.log('X'.repeat(this.w));
    }
  }

  rotate () {
    const tmp = this.w;
    this.w = this.h;
    this.h = tmp;
  }

  double () {
    this.w *= 2;
    this.h *= 2;
  }
}
module.exports = Rectangle;
