#!/usr/bin/node
// a script to print a sqaure

const rep = process.argv[2];
const num = parseInt(rep);
let word = '';

if (isNaN(num)) {
  console.log('Missing size');
  process.exit();
} else {
  for (let i = 0; i < num; i++) {
    word = '';
    for (let j = 0; j < num; j++) {
      word += 'X';
    }
    console.log(word);
  }
}
