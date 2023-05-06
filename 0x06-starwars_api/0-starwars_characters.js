#!/usr/bin/node

/**
 * prints characteres in a star wars movie as listed in the /films/ endpoint
 */

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, async (err, response, body) => {
  if (err) return console.error(err);
  const charUrlList = JSON.parse(body).characters;
  for (const charUrl of charUrlList) {
    await new Promise((resolve, reject) => {
      request(charUrl, (err, response, body) => {
        if (err) return console.error(err);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
