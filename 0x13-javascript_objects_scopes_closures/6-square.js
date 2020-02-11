#!/usr/bin/node
// instance method called charPrint(c)

const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let h = 1; h <= this.width; h++) {
        for (let w = 1; w <= this.width; w++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
}
module.exports = Square;
