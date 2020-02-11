#!/usr/bin/node
// rotate() exchanges the width - the height and double() multipliq 2

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

  rotate () {
    const auxHeight = this.height;
    this.height = this.width;
    this.width = auxHeight;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
