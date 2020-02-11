#!/usr/bin/node

const uri = 'https://jsonplaceholder.typicode.com/todos?completed=true';
const request = require('request');

request(uri, (error, _, body) => {
  if (!error) {
    const elements = JSON.parse(body);
    const ids = [...new Set(elements.map(x => x.userId))];
    const out = {};
    for (const id of ids) {
      out[id] = elements.filter(x => x.userId === id).length;
    }
    console.log(out);
  } else console.log(error);
});
