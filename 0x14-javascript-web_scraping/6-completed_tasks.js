#!/usr/bin/node
/**
 * computes the number of tasks completed by user id
 * - the first argument is the API URL:
 *   https://jsonplaceholder.typicode.com/todos
 * - only prints users with completed tasks
 * - you must use the module request
 */
const request = require('request');

if (process.argv.length === 2) {
  process.exit(1);
}

const URL = process.argv[2];

request(URL, { json: true }, function (err, response) {
  if (err) {
    process.exit(1);
  }

  const usersLog = {};

  for (const value of response.body) {
    if (value.completed) {
      usersLog[value.userId] = (usersLog[value.userId] || 0) + 1;
    }
  }
  console.log(usersLog);
});
