#!/usr/bin/node
/**
 * prints the title of a Star Wars movie where the episode number
 * matches a given interger
 * - the first argument is the movie ID
 * - you must use the Star wars API with the endpoint
 *   https://swapi-api.alx-tools.com/api/films/:id
 * - you must use the module request
 */
const request = require('request');

if (process.argv.length === 2) {
  process.exit(1);
}

const id = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(URL, { json: true }, function (err, response) {
  if (err) {
    process.exit(1);
  } else {
    console.log(response.body.title);
  }
});
