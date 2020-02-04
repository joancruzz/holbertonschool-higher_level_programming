#!/usr/bin/node
// print process.argv
const length = parseInt(process.argv.length);
if (length >= 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
