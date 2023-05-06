#!/usr/bin/node

/**
 * prints characteres in a star wars movie as listed in the /films/ endpoint
 */


const request = require('request')

movie_id = process.argv[2]
url = `https://swapi.dev/api/films/${movie_id}/`

request(url, async (err, response, body) => {
    if (err) return console.error(err);
    const char_url_list = JSON.parse(body).characters;
    for (const char_url of char_url_list) {
        await new Promise((resolve, reject) => {
            request(char_url, (err, response, body) => {
                if (err) return console.error(err);
                console.log(JSON.parse(body).name);
                resolve();
            });
        });
    };
});


