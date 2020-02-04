#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const myVar = process.argv.slice(2);
const a = parseInt(myVar[0], 10);
const b = parseInt(myVar[1], 10);
console.log(add(a, b));
