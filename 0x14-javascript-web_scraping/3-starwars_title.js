#!/usr/bin/node
// prints the title of a Star Wars movie with movie ID

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, 'utf-8', function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
