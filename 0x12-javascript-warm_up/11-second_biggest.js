#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const sorted = args.sort().reverse();
  for (let i = 0; i < sorted.length; i++) {
    if (i === sorted.length - 1) {
      console.log(sorted[i]);
      break;
    } else if (sorted[i + 1] < sorted[i]) {
      console.log(sorted[i + 1]);
      break;
    } else {
      continue;
    }
  }
}
