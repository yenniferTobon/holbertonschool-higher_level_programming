#!/usr/bin/node
// script that computes and prints a factorial

const num = parseInt(process.argv[2]);

function factorial (a) {
  if (a === 1) {
    return (1);
  }else {
    const totalFactorial = (a * factorial (a - 1));
    return (totalFactorial);
  }
}

console.log(factorial(num));
