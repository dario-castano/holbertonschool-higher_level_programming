#!/usr/bin/node

const uri = 'http://swapi.co/api/people/18';
const request = require('request');

request(uri, (error, _, body) => {
  if (!error) console.log(JSON.parse(body).films.length);
  else console.log(error);
});
