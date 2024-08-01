#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
const requestURL = process.argv[2];
const ID = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request({ url: requestURL, json: true }, (error, response) => {
  if (error) {
    console.error(error);
  }
  for (const value of response.body.results) {
    for (const character of value.characters) {
      if (ID === character) {
        count += 1;
      }
    }
  }
  console.log(count);
});
