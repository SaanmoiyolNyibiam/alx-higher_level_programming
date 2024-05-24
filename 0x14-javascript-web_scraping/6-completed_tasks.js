#!/usr/bin/node
/**
 * computes the number of tasks completed by user id
 * - he first argument is the API URL:
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
    console.log(err);
    process.exit(1);
  }

  const usersLog = {};
  for (const user of response.body) {
    usersLog[user.userId] = 0;
  }

  for (const value of response.body) {
    for (const user in usersLog) {
      if (+user === value.userId && value.completed) {
        usersLog[user] += 1;
      }
    }
  }
  console.log(usersLog);
});
