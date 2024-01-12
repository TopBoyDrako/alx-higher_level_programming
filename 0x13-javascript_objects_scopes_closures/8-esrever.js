#!/usr/bin/node

exports.esrever = function (list) {
  function rev (arr) {
    const reversedArray = [];

    for (let i = arr.length - 1; i >= 0; i--) {
      reversedArray.push(arr[i]);
    }

    return reversedArray;
  }

  return rev(list);
};
