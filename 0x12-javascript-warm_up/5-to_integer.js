#!/usr/bin/node
// convert argument with parseInt if you can't isNaN

const argument = parseInt(process.argv[2]);

if (isNaN(argument)) {
  console.log('Not a number');
} else if (typeof argument === 'number') {
  console.log('My number: ' + argument);
} else {
  console.log('Not a number');
}
