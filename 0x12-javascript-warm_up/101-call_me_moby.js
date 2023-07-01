#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let index;
  for (index = 0; index < x; index++) {
    theFunction();
  }
};
