#!/usr/bin/node

dict = require('./101-data').dict;
const freqs = [... new Set(Object.values(dict).sort())];
let out = {};

for (f of freqs) {
  out[f] = Array();
}

for (key of Object.keys(dict)) {
  for (freq of freqs) {
    if (dict[key] === freq) {
      arr = out[freq];
      arr.push(key);
      out[freq] = arr;
    }
  }
}

console.log(out);
