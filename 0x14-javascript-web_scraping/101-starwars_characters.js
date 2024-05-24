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
const request = require('request');

if (process.argv.length === 2) {
  process.exit(1);
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

function requestGet (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, function (err, response) {
      if (err) {
        reject(err);
      } else {
        resolve(response.body);
      }
    });
  });
}

async function fetchCaracters (url) {
  try {
    const fResponse = await requestGet(url);
    const characters = fResponse.characters;

    for (const character of characters) {
      const cResponse = await requestGet(character);
      console.log(cResponse.name);
    }
  } catch (err) {
    process.exit(1);
  }
}

fetchCaracters(url);
