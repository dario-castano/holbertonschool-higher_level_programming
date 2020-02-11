#!/usr/bin/node

const uri = process.argv[2];
const id = 18;
const term = `https:${uri.slice(5, 20)}people/${id}/`
const request = require('request');

request(uri, (error, _, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    const out = results.map(x => x.characters).filter(x => x.includes(term));
    console.log(out.length);
  } else console.log(error);
});
