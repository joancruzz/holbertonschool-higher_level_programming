#!/usr/bin/node
// Function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce(function (n, val) {
    return (n + (val === searchElement));
  }, 0);
  return count;
};
