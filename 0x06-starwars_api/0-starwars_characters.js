#!/usr/bin/node
/**
 * Get the Star Wars characters from the API
 *  */ 
const request = require('request');
const filmId = process.argv[2];
let characters;
if (!filmId || isNaN(filmId)) {
    process.exit(1);
  }
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(error);

  // Printing body
  characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (error, response, body) => {
      if (error) console.log(error);
      // console.log(response.statusCode);
      console.log(JSON.parse(body).name);
    });
  }
});
