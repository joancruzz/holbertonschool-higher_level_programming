#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numArr = process.argv.slice(2).sort((a, b) => a - b);
  console.log(numArr[numArr.length - 2]);
}
