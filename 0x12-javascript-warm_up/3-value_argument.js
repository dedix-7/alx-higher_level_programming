#!/usr/bin/node
// a script to print the first conmmandline argument

const arrayCmd = process.argv;

if ((arrayCmd[2] === undefined)) {
  console.log('No argument');
} else {
  console.log(arrayCmd[2]);
}
