#!/usr/bin/node
// A script that imports an array and computes a new array.

let list = require('./100-data').list;
console.log(list);
console.log(list.map((element, index) => element * index));
