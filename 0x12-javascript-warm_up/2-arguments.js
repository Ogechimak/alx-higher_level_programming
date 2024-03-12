#!/usr/bin/node
if (process.argv.length < 10) {
  console.log('No argument');
} else if (process.argv.length === 10) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
