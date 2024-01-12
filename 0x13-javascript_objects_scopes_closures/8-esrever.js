#!/usr/bin/node

exports.esrever = function (list) {
  function reverse (arr) {
    const reversedArray = [];

    for (let i = arr.length - 1; i >= 0; i--) {
      reversedArray.push(arr[i]);
    }

    return reversedArray;
  }

  return reverse(list);
};
