#!/usr/bin/node

const filmId = process.argv[2];
const uri = `http://swapi.co/api/films/${filmId}`;
const request = require('request');

request(uri, (error, _, body) => {
  if (!error) console.log(JSON.parse(body).title);
  else console.log(error);
});
