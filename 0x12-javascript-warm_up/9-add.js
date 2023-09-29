#!/usr/bin/node

function add (x, y) {
  return x + y;
}
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
