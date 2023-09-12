#!/usr/bin/node
let j = 0;
exports.logMe = function (item) {
  console.log(j + ': ' + item);
  j++;
};
