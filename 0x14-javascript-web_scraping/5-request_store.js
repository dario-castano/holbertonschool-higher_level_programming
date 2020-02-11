#!/usr/bin/node

const uri = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request(uri, (error, _, body) => {
  if (!error) {
    fs.writeFile(file, body, err => {
      if (err) console.log(error);
    });
  } else {
    console.log(error);
  }
});
