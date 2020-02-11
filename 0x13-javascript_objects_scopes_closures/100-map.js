#!/usr/bin/node
// Write a script that imports an array and computes a new array.
const list = require('./100-data').list;
console.log(list);
const map = list.map((x, i) => x * i);
console.log(map);
