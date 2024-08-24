#!/usr/bin/node
// a script to get commandline arguments

const arrayCmd = process.argv;

if ((arrayCmd.length === 2)) {
  console.log('No argument');
} else if ((arrayCmd.length === 3)) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
