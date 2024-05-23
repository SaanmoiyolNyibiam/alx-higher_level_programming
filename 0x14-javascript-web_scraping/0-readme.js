#!/usr/bin/node
/**
 * this is a script that reads and prints the content of a file
 * - the first argument is the file path
 * - the content of the file must be read in utf
 * - if an error occured during the reading, print the error object
 */
const fs = require('fs');

if (process.argv.length === 2) {
  process.exit(1);
}

const filePath = process.argv[2];
fs.readFile(filePath, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
