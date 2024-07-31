#!/usr/bin/node
//A script that reads and prints the content of a file.


const fs = require('fs');
fileName = process.argv[2];
fs.readFile(fileName, 'utf8', (err, data) => {
    if (err)
    {
        console.error(err);
        return;
    }
    console.log(data);
})
