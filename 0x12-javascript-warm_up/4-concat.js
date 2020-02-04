#!/usr/bin/node
// prints two arguments passed to it, in the following format: “ is ”

const numVarible = process.argv.length;

if (numVarible > 2) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (numVarible === 2) {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
