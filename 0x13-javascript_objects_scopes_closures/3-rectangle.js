#!/usr/bin/node
// Create an instance method called print() that prints the rectangle with X

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) {
      return 'undefined';
    }
    if (w === 0 || h === 0) {
      return 0;
    }
    if (w <= 0 || h <= 0) {
      return 0;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let h = 1; h <= this.height; h++) {
      for (let w = 1; w <= this.width; w++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}
module.exports = Rectangle;
