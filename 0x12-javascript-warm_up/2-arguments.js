#!/usr/bin/node
// print process.argv
const length = parseInt(process.argv.length);
if (length >= 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
