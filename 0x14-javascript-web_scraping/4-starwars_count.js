#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
const requestURL = 'https://swapi-api.alx-tools.com/api/films';
const ID = '18';
let count = 0;

request({ url: requestURL, json: true }, (error, response) => {
  if (error) {
    console.error(error);
  }
  for (const value of response.body.results) {
    for (const character of value.characters) {
      if (ID === character.split('/')[5]) {
        count += 1;
      }
    }
  }
  console.log(count);
});
