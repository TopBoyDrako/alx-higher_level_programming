#!/usr/bin/node

const { dict } = require('./101-data');

const newUserIdsByOccurrence = Object.entries(dict).reduce((result, [userId, occurrences]) => {
  result[occurrences] = (result[occurrences] || []).concat(userId);
  return result;
}, {});

console.log(newUserIdsByOccurrence);
