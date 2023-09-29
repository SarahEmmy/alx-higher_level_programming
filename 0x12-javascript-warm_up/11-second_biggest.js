#!/usr/bin/node

const len = process.argv.length - 2;
const array = process.argv.slice(2);
if (len <= 1) {
  console.log('0');
} else {
  array.sort((x, y) => {
    return x - y;
  });
  console.log(array[len - 2]);
}
