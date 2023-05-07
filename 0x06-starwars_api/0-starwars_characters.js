#!/usr/bin/node
// prints all the characters for a particular starwars movie

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (err, response, body) {
      if (error) {
        return console.error(error);
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
