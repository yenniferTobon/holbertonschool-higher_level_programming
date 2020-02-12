#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, 'utf-8', function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const r = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < r.length; i++) {
      const ch = r[i].characters;
      for (let j = 0; j < ch.length; j++) {
        if (ch[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
