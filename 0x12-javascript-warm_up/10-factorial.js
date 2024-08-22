#!/usr/bin/node
// a script to calculate the factorial

const num = parseInt(process.argv[2]);

function fact (tree) {
  if (isNaN(tree)) {
    return (1);
  } else if ((tree === 0) || (tree === 1)) {
    return (1);
  } else {
    return (tree * fact(tree - 1));
  }
}
console.log(fact(num));
