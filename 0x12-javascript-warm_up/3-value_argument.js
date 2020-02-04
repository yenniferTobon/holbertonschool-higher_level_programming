#!/usr/bin/node
// prints the first argument passed to it

process.argv.forEach((element, numVarible) => {
  if (`${numVarible}` > 1) {
    console.log(`${element}`);
  }
});

if (process.argv[2] === undefined) {
  console.log('No argument');
}
