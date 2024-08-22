#!/usr/bin/node
// a script to find the second biggest number in an array

const original = process.argv;

function second (argum) {
  let largest = argum[0];
  let sec = -Infinity;

  for (let i = 0; i < argum.length; i++) {
    if (argum[i] > largest) {
      sec = largest;
      largest = argum[i];
    } else if ((argum[i] > sec) && (argum[i] !== largest)) {
      sec = argum[i];
    }
  }
  return (sec);
}

if (original.length === 2) {
  console.log(0);
  process.exit();
} else if (original.length === 3) {
  console.log(0);
  process.exit();
} else {
  const placehold = original.slice(2);
  const current = placehold.map(Number);
  console.log(second(current));
}
