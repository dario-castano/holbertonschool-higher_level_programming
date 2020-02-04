#!/usr/bin/node
const args = process.argv.slice(2);
const n = parseInt(args[0], 10);
if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + n);
}
