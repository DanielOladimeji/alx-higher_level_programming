#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const UserId in dict) {
  if (dict[UserId] in newDict) {
    newDict[dict[UserId]].push(UserId);
  } else {
    newDict[dict[UserId]] = [UserId];
  }
}
console.log(newDict);
