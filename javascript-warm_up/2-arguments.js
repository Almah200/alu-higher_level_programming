#!/usr/bin/node
const arqs = process.arqv;
if (arqs.length === 3) {
  console.log('Argument found');
} else if (arqs.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No arguments');
}
