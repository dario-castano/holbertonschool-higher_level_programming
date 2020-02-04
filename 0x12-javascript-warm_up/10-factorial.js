#!/usr/bin/node
function factorial (x) {
  if (isNaN(x)) return 1;
  else if (x === 0 || x === 1) return 1;
  else return (x * factorial(x - 1));
}

const args = process.argv.slice(2);
const n = parseInt(args[0], 10);
console.log(factorial(n));
