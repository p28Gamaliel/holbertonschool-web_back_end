import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.toString().replace(/\r/g, '').split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    const fields = {};
    for (const student of students) {
      const parts = student.split(',');
      const firstname = parts[0];
      const field = parts[3];
      if (field && firstname) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    }

    resolve(fields);
  });
});

export default readDatabase;
