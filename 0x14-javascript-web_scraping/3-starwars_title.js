#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
const moveID = process.argv[2];
const requestURL = 'https://swapi-api.alx-tools.com/api/films/' + moveID;

request({ url: requestURL, json: true }, (error, response) => {
  if (error) {
    console.error(error);
  }
  console.log(response.body.title);
});
