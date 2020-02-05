#!/usr/bin/node
// prints a square, first argument is the size

const argument = parseInt(process.argv[2]);

if ((isNaN(argument)) || process.argv.lenght === 1) {
  console.log('Missing size');
} else if (typeof argument === 'number') {
  for (let aux = 0; aux < argument; aux++) {
    let concat = '';
    for (let aux = 0; aux < argument; aux++) {
      concat = concat + 'X';
    }
    console.log(concat);
  }
}
