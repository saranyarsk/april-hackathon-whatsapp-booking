const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Function to log messages to a file
function logMessage(from, body) {
  const logFilePath = path.join(__dirname, 'messages.log');
  const logMessage = `From: ${from}, Message: ${body}\n`;
  fs.appendFile(logFilePath, logMessage, (err) => {
    if (err) {
      console.error('Error writing to log file:', err);
    }
  });
}

app.post('/webhook', async (req, res) => {
  try {
    const { from, body } = req.body;
    console.log('Received message from:', from);
    console.log('Message:', body);
    
    // Log the message to a file
    logMessage(from, body);

    // Here you can add code to identify the customer and handle the message

    res.json({ status: 'success' });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ status: 'error', message: 'Internal server error' });
  }
});

app.use(express.static('public'));

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
