#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
};

const getCharacterName = async (characterUrl) => {
  try {
    const response = await makeRequest(characterUrl);
    const character = JSON.parse(response);
    console.log(character.name);
  } catch (err) {
    console.log(err);
  }
};

const processCharacters = async () => {
  try {
    const response = await makeRequest(url);
    const film = JSON.parse(response);
    const charactersArray = film.characters;

    for (const character of charactersArray) {
      await getCharacterName(character);
    }
  } catch (err) {
    console.log(err);
  } finally {
    process.exit();
  }
};

processCharacters();
