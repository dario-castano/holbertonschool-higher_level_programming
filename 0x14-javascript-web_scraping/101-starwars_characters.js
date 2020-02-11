#!/usr/bin/node

const uri = process.argv[2];
const request = require('request');

request(uri, (error, response, body) => {
  if (!error) console.log('code: ' + response.statusCode);
  else console.log(error);
});
