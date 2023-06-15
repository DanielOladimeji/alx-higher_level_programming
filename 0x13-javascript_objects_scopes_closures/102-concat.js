#!/usr/bin/node
const fs = require('fs');
const inFileA = fs.readFileSync(process.argv[2], 'utf-8');
const inFileB = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFile(process.argv[4], inFileA + inFileB, err => {
  if (err) {
    console.log(err);
  }
});
