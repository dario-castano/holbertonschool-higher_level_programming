#!/usr/bin/node

const dict = require('./101-data').dict;
const freqs = [...new Set(Object.values(dict).sort())];
const out = {};

for (const f of freqs) {
  out[f] = [];
}

for (const key of Object.keys(dict)) {
  for (const freq of freqs) {
    if (dict[key] === freq) {
      const arr = out[freq];
      arr.push(key);
      out[freq] = arr;
    }
  }
}

console.log(out);
