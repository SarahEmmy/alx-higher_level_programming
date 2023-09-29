#!/usr/bin/node

const squareSize = Number(process.argv[2]);

if (Number(process.argv[2])) {
  let j = 0;

  for (j; j < squareSize; j++) {
    console.log('X'.repeat(squareSize));
  }
} else {
  console.log('Missing size');
}
