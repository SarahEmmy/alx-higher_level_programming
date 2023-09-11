#!/usr/bin/node

let j = 0;
if (process.argv[2]) {
  for (j; j < process.argv[2]; j++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrencest');
}
