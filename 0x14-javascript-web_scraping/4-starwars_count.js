#!/usr/bin/node

const uri = process.argv[2];
const id = 'https://swapi.co/api/people/18/';
const request = require('request');

request(uri, (error, _, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    const out = results.map(x => x.characters).filter(x => x.includes(id));
    console.log(out.length);
  } else console.log(error);
});
