#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const fs = require('fs');
const request = require('request');
const requestURL = process.argv[2];
const filePath = process.argv[3];

request(requestURL, (error, response) => {
  if (error) {
    console.error(error);
  }
  fs.writeFile(filePath, response.body, 'utf8', err => {
    if (err) {
      console.error(err);
    }
  });
});
