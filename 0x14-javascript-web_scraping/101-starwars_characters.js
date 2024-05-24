#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie
 * - the first argument is the Movie, example: 3 = "Return of the Jedi"
 * display
 * - displays one character name by line
 *   in the same order of the list “characters”
 *   in the /films/ response
 * - you must use the Star wars API
 * - you use the modult request
 */
const rp = require('request-promise');

if (process.argv.length === 2) {
  process.exit(1);
}

const ID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;

async function fetchCaracters () {
  try {
    const fResponse = await rp({ uri: URL, json: true });
    const characters = fResponse.characters;

    for (const character of characters) {
      const cResponse = await rp({ uri: character, json: true });
      console.log(cResponse.name);
    }
  } catch (err) {
    process.exit(1);
  }
}

fetchCaracters();
