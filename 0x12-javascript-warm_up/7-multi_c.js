#!/usr/bin/node
// prints x times “C is fun”

const argument = parseInt(process.argv[2]);

if ((isNaN(argument)) || (process.argv.length === 0)) {
  console.log('Missing number of occurrences');
} else if (typeof argument === 'number') {
  for (let aux = 0; aux < argument; aux++) {
    console.log('C is fun');
  }
}
