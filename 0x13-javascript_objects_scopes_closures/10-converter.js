#!/usr/bin/node
exports.converter = function (base) {
  return function (convertNum) {
    return (convertNum.toString(base));
  };
};
