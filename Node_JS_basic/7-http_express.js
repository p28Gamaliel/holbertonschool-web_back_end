const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.toString().replace(/\r/g, '').split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      let output = `Number of students: ${students.length}\n`;

      const fields = {};
      for (const student of students) {
        const [firstname, , , field] = student.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }

      const fieldEntries = Object.entries(fields);
      fieldEntries.forEach(([field, names], index) => {
        output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        if (index < fieldEntries.length - 1) {
          output += '\n';
        }
      });

      resolve(output);
    });
  });
}

const database = process.argv[2];

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(database)
    .then((output) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((error) => {
      res.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245);

module.exports = app;
