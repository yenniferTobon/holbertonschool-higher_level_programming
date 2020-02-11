#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const newList = [];
  for (let aux = 0; aux < list.length; aux++) {
    newList.unshift(list[aux]);
  }
  return newList;
};
