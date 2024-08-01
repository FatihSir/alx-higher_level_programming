#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');
const requestURL = process.argv[2];
const users = {};

request({ url: requestURL, json: true }, (error, response) => {
  if (error) {
    console.error(error);
  }
  for (const user of response.body) {
    if (user.completed === true) {
      if (!users[user.userId]) {
        users[user.userId] = 1;
      } else { users[user.userId] = users[user.userId] + 1; }
    }
  }
  console.log(users);
});
