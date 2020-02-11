#!/usr/bin/node
// Script that display the status code of a GET request
const request = require('request');

request(process.argv[2], { json: true }, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
