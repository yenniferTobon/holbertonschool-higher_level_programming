#!/usr/bin/node
// prints a message with the number of arguments passed

const numVarible = process.argv.length - 2;

if (numVarible === 0) {
  console.log('No argument');
} else if (numVarible === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
