#!/usr/bin/node
// converts a number from base 10 to another base

exports.converter = function (base) {
  return function (convert) {
    return convert.toString(base);
  };
};
