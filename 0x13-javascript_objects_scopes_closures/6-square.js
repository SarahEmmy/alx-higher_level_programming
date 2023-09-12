#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let j = 0;
    for (j; j < this.h; j++) {
      console.log(c.repeat(this.w));
    }
  }
}
module.exports = Square;
