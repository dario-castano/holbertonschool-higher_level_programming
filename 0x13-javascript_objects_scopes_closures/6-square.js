#!/usr/bin/node

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    if (c === undefined) super.print();
    else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
