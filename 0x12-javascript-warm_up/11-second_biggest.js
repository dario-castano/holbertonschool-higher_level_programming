#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const sorted = [...new Set(args.sort().reverse())];
  console.log(sorted[1])
}
