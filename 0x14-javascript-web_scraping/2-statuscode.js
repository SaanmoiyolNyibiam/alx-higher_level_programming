#!/usr/bin/node
/**
 * displays the status code of a GET request
 * - the first argument is the URL to request(GET)
 * - the status code must be printed like this: code: <status code>
 * - you must use the module request
 */
const request = require('request');

if (process.argv.length === 2) {
  process.exit(1);
}

const URL = process.argv[2];

request(URL, function (err, response) {
  if (!err) {
    console.log(`code: ${response.statusCode}`);
  }
});
