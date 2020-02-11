#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  const sizeList = list.length;
  let occurrences = 0;
  for (let i = 0; i < sizeList; i++) {
    if (list[i] === searchElement) {
      occurrences = occurrences + 1;
    }
  }
  return occurrences;
};
