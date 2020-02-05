#!/usr/bin/node
// Script that prints the first argument passed to it
const third = process.argv[2];
if (third) {
  console.log(third);
} else {
  console.log('No argument');
}
