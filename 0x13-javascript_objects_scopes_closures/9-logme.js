#!/usr/bin/node
// Print number of arguments already printed
// and the new argument value
global.count = 0;
exports.logMe = function (item) {
  console.log(global.count + ': ' + item);
  global.count += 1;
};
