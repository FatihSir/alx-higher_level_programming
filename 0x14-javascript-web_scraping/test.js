#!/usr/bin/node
// A script that writes a string to a file.

const fetch = require('node-fetch');

const urlRequest = "https://alx-intranet.hbtn.io/status";

fetch(urlRequest)
    .then(response => response.text())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
