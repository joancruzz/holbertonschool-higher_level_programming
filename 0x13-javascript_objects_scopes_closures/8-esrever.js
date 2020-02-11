#!/usr/bin/node
// Function that returns the reversed version of a list
exports.esrever = function (list) {
  const newArr = [];
  let i = list.length - 1;
  for (i; i >= 0; i--) {
    newArr.push(list[i]);
  }
  return newArr;
};
