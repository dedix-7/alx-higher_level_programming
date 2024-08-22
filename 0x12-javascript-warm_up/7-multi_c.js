#!/usr/bin/node
// a script to print multiple lamguages

const rep = process.argv[2];
const num = parseInt(rep);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
  process.exit();
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
