#!/usr/bin/node

const uri = process.argv[2];
const id = '18';
const request = require('request');

request(uri, (error, _, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    const out = results
      .map(x => x.characters.map(y => y.slice(28).replace('/', '')))
      .filter(x => x.includes(id));
    console.log(out.length);
  } else console.log(error);
});
