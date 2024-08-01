#!/usr/bin/node
// A script that prints all characters of a Star Wars movie.

const request = require('request');
const requestURL = 'https://swapi-api.alx-tools.com/api/films/';
const movieID = process.argv[2];

function getCharacter (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (err, response, body) => {
      if (err) {
        return reject(err);
      }
      try {
        const name = JSON.parse(body).name;
        resolve(name);
      } catch (parseError) {
        reject(parseError);
      }
    });
  });
}

request(requestURL, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const movies = JSON.parse(body).results;
  const chars = movies[movieID - 1].characters;
  const characterPromises = chars.map(getCharacter);

  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => {
        console.log(name);
      });
    })
    .catch(error => {
      console.error(error);
    });
});
