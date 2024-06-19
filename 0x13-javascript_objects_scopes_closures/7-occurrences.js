#!/usr/bin/node
// A function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  if (list === undefined || searchElement === undefined) return 0;
  let n = 0;
  list.forEach((element) => { if (element === searchElement) n++; });
  return n;
};
