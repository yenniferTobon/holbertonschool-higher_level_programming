#!/usr/bin/node
// script that reads and prints the content of a file.

var fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  } else {
    console.log(data);
  }
});
