#!/usr/bin/node
// Script that prints the number of movies
// where the character “Wedge Antilles” is present
const request = require('request');
const url = 'http://swapi.co/api/people/18/';

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.films.length);
  }
});
