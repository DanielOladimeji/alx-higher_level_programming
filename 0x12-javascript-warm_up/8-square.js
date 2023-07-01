#!/usr/bin/node
const num = parseInt(process.argv[2]);
let i;
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (i = 1; i <= nmu; i++) {
    console.log('X'.repeat(num));
  }
}
