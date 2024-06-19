#!/usr/bin/node
// A function that returns the reversed version of a list

exports.esrever = function (list) {
  if (list === undefined) return [];
  const reversed = [];
  for (let l = list.length - 1; l >= 0; l--) {
    reversed.push(list[l]);
  }
  return reversed;
};
