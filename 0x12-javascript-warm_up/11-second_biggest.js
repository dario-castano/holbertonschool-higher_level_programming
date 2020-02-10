#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const arr = args.map(
    x => parseInt(x)
  ).sort(
    (a, b) => b - a
  );
  const sorted = [...new Set(arr)];
  console.log(sorted[1]);
}
