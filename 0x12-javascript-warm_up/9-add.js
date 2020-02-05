#!/usr/bin/node
// prints the addition of 2 integers

const numVarible = process.argv.length - 2;

if (numVarible <= 1) {
  console.log('NaN');
} else {
  console.log(add(process.argv[2], process.argv[3]));
}

function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  return (sum);
}
