#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie
 * - the first argument is the Movie, example: 3 = "Return of the Jedi"
 * display
 * - displays one character name by line
 * - you must use the Star wars API
 * - you use the modult request
 */
const request = require('request');

if (process.argv.length === 2) {
  process.exit(1);
}

const ID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request(URL, { json: true }, function (err, response) {
  if (err) {
    process.exit(1);
  }
  const characters = response.body.characters;
  for (const character of characters) {
    request(character, { json: true }, function (err, response) {
      if (err) {
        process.exit(1);
      }
      console.log(response.body.name);
    });
  }
});
