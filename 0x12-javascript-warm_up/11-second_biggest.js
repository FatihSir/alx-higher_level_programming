#!/usr/bin/node
// a script that searches the second biggest
// integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
const args = process.argv.slice(2);
const list = args.map(Number).sort((a, b) => a - b);
console.log(list[list.length - 2]);
}

