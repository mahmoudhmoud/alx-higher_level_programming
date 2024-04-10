#!/usr/bin/node

// adk as monj
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
