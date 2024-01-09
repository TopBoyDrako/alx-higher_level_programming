#!/usr/bin/node

const script = parseInt(process.argv[2]);

if (isNaN(script)) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  while (i < script) {
    console.log('C is fun');
    i++;
  }
}
