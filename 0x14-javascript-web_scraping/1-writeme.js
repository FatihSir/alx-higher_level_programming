#!/usr/bin/node
// A script that writes a string to a file.

const fs = require('fs');
const fileName = process.argv[2];
const content = process.argv[3];

fs.writeFile(fileName, content, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
