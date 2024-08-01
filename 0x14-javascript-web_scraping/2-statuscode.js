#!/usr/bin/node
// A script that display the status code of a GET request.

const requestURL = process.argv[2];
const request = require('request');

request.get(requestURL, (error, response) => {
  if (error) {
    console.error(error);
  }
  console.log('code:', response.statusCode);
});
