const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Mock identifyCustomer function
async function identifyCustomer(phoneNumber) {
  return {
    name: 'John Doe',
    phoneNumber: phoneNumber
  };
}

app.post('/webhook', async (req, res) => {
  try {
    const { from, body } = req.body;
    const customer = await identifyCustomer(from);
    console.log('Identified Customer:', customer);
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
