#!/usr/bin/node
// A script that imports a dictionary of occurrences by
// user id and computes a dictionary of user ids by occurrence.

const dict = require('./101-data').dict;
let myDict = {};
let k;
for (k in dict) {
  myDict[dict[k]] = [];
}
for (k in dict) {
  myDict[dict[k]].push(k);
}
function cmp (a, b) {
  return a - b;
}
for (k in myDict) {
  myDict[k].sort(cmp);
}
console.log(myDict);
