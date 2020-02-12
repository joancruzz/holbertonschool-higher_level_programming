#!/usr/bin/node
// Script that prints the title of a Star Wars movie
// where the episode number matches a given integer
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, { json: true }, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body.title);
  }
});
