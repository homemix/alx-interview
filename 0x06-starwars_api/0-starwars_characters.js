#!/usr/bin/node
/**
 * Star wars api
 * Script that prints all characters of a Star Wars movie:
 */
const request = require('request');
const filmId = process.argv[2];
if (!filmId || isNaN(filmId)) {
  process.exit(1);
}
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

const movieCharacters = new Promise((resolve, reject) => {
  request(url, (error, response, body) => {
    if (error) reject(error);
    resolve(JSON.parse(body).characters);
  });
}
);

movieCharacters.then((characters) => {
  // console.log(characters);
  characters.forEach(element => {
    request(element, (error, response, body) => {
      if (error) console.log(error);
      console.log(JSON.parse(body).name);
    });
  });
}
).catch((error) => {
  console.log(error);
}
);
