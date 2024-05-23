#!/usr/bin/node
/**
 * gets the contents of a webpage and stores it in a file
 * - the first argument is the URL to request
 * - the second argument is the file path to store the body response
 * - the file must be UTF-8 encoded
 * - you must use the module request
 */
const request = require('request');
const fs = require('fs');

if (process.argv.length === 2) {
  process.exit(1);
}

const URL = process.argv[2];
const filePath = process.argv[3];
request(URL, function (err, response) {
  if (err) {
    process.exit(1);
  }
  fs.writeFile(filePath, response.body, function (err) {
    if (err) {
      process.exit(1);
    }
  });
});
