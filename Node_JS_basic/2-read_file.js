const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, 'utf-8');

    const lines = content.split('\n').filter((line) => line.trim() !== '');

    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    const studentLines = lines.slice(1);
    
    console.log(`Number of students: ${studentLines.length}`);

    const fields = {};

    for (const line of studentLines) {
      const studentData = line.split(',');
      const firstName = studentData[0];
      const field = studentData[3];

      if (field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    }

    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }

  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
