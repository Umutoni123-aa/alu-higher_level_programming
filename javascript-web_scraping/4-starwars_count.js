#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const film of results) {
      if (film.characters.find(char => char.includes('/18/'))) {
        count++;
      }
    }
    console.log(count);
  }
});
