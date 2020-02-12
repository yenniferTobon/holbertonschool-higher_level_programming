#!/usr/bin/node
// script that writes a string to a file

var fs = require('fs');

var data = process.argv[3];
fs.writeFile(process.argv[2], data, function (err) {
  if (err) {
    console.log(err);
  }
});
