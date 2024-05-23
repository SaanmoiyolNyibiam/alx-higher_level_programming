#!/usr/bin/node
/**
 * prints the number of movies where the character "Wedge Antilles"
 * is present
 *  - the first argument is the API URL of the Star wars API:
 *    https://swapi-api.alx-tools.com/api/films/
 *  - Wedge Antilles is character ID 18 - your script must use this
 *    ID for filtering the result of the API
 *  - You must use the module request
 */
const request = require('request');

if (process.argv.length === 2) {
  process.exit(1);
}

const URL = process.argv[2];
let movieCount = 0;
const regx = /[*]*18/;

request(URL, { json: true }, function (err, response) {
  if (err) {
    process.exit(1);
  }

  const films = response.body.results;
  for (const film of films) {
    // console.log(film.characters)
    for (const actor of film.characters) {
      if (regx.test(actor)) {
        movieCount += 1;
      }
    }
  }
  console.log(movieCount);
});
