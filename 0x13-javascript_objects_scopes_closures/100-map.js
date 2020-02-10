#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);
const newlist = list.map(x => x * list.indexOf(x));
console.log(newlist);
