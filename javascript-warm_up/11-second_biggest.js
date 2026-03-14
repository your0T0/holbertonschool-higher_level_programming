#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a);
  const unique = [...new Set(sorted)];
  console.log(unique[1] || 0);
}
