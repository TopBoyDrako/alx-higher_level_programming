#!/usr/bin/node

const script = 'C is fun';
let i = 0;

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  while (i < parseInt(process.argv[2])) {
    console.log(script[i]);
    i++;
  }
}
