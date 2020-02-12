#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const info = JSON.parse(body);
    let counter = 0;
    for (let i = 0; i < info.results.length; i++) {
      for (let guy = 0; guy < info.results[i].characters.length; guy++) {
        if (info.results[i].characters[guy].includes('/18/')) {
          counter += 1;
          break;
        }
      }
    }
    console.log(counter);
  }
});
