#!/usr/bin/node
// a script to print the first conmmandline argument

const arrayCmd = process.argv;
const num = parseInt(arrayCmd[2]);
// const num = repl.replace(/,/g, '');

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
