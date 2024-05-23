#!/usr/bin/node
/**
 * writes a string to a file
 * - the first argument is the file path
 * - the second argument is the string to write
 * - the content of the file must be written in utf-8
 * - if an error occured while writing, print the error object
 */
const fs = require('fs');

if (process.argv.length === 2) {
  process.exit(1);
}

const filePath = process.argv[2];
const data = process.argv[3];
const encoding = 'utf-8';

fs.writeFile(filePath, data, encoding, function (err) {
  if (err) {
    console.log(err);
  }
});
