#!/usr/bin/node
const myVar = process.argv.slice(2);
const n = parseInt(myVar[0], 10);
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
