#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(erorr);
  } 
  if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    tasks.forEach((task => {
      if (task.completed === true) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    });
    console.log(completed);
  } 
  else {
    console.error(`An error occurred. Status code: ${response.statusCode}`);
  }
});
