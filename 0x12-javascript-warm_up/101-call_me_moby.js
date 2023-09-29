#!/usr/bin/node

exports.callMeMoby = function (xNum, theFunction) {
  let j = 0;
  for (j; j < xNum; j++) {
    theFunction();
  }
};
