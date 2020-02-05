#!/usr/bin/node
// Script that prints two arguments passed to it
const first = process.argv[2];
const third = process.argv[3];
if (first && third) {
  console.log(first + ' is ' + third);
}
