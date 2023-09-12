#!/usr/bin/node
exports.esrever = function (list) {
  const revsList = [];

  for (let j = list.length - 1; j >= 0; j--) {
    revsList.push(list[j]);
  }
  return revsList;
};
