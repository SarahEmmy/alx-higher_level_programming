#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.w = width;
      this.h = height;
    }
  }
}
module.exports = Rectangle;
