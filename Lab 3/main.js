const express = require('express');
const path = require('path');

const app = express();
const PORT = 3500;

favNum = 0;

const inventory = {
  1: { id: 1, name: 'Laptop', price: 999.99 },
  2: { id: 2, name: 'Phone', price: 499.99 },
  3: { id: 3, name: 'Tablet', price: 299.99 }
};

// Middleware to parse JSON request bodies
app.use(express.json());

// For parsing application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));
// app.usse("/public", express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.status(200);
    res.send("Welcome to the Express.js server!");
});

// 1 - HTML Content
app.get('/about', (req, res) => {
    res.status(200);
    res.send("<h3>This web server has 10 Express.js routes!</h3>");
});

// 2- Query parameters - HTML Content
app.get('/helloname', (req, res) => {
    const name = req.query.name || 'Guest'; // Fallback if no name provided
    res.status(200).send(`<h3>Hello, ${name}!</h3>`);
});

// 3- Query Parameters - HTML Content
app.get('/favoritenumber', (req, res) => {
    favNum = req.query.number
    res.status(200).send(`<h3>Your favorite number, ${favNum}, has been saved!</h3>`);
});

// 4 - Query Parameters - Headers
app.get('/inventory', (req, res) => {
    const itemId = req.query.item; 
    const item = inventory[itemId];

    res.status(200).json(item);
});

// 5 - Post request - HTML Content
app.post('/processpayment', (req, res) => {
    const valid_card_number = 1234567890123456;
    const valid_cvv = 123;
    const minimum_amount = 20;

    const the_card_number = req.headers['x-card-number']
    const the_cvv = req.headers['x-cvv'];
    const the_amount = req.headers['x-amount'];

    if (the_card_number == valid_card_number && the_cvv == valid_cvv && the_amount >= minimum_amount) {
        res.status(200).send("<h3>Payment processed successfully!</h3>");
    } else {
        res.status(400).send("<h3>Payment failed. Please check your card details and amount.</h3>");
    }

});

// 6 - Query Parameters - HTML Content
app.get('/guessTheNumber', (req, res) => {
    const number = parseInt(req.query.number, 10);
    const randomNumber = Math.floor(Math.random() * 10) + 1;

    if (number === randomNumber) {
        res.status(200).send(`<h3>Congratulations! You guessed the number ${randomNumber} correctly!</h3>`);
    } else {
        res.status(200).send(`<h3>Wrong! The correct number was ${randomNumber}.</h3>`);
    }
});

// 7 - Query Parameters
app.get('/addition', (req, res) => {
    const num1 = parseFloat(req.query.num1);
    const num2 = parseFloat(req.query.num2);

    const sum = num1 + num2;
    res.status(200).send({sum});
});

// 8 - Headers
app.get('/subtraction', (req, res) => {
    const num1 = parseFloat(req.headers['x-num1']);
    const num2 = parseFloat(req.headers['x-num2']);

    const difference = num1 - num2;
    res.status(200).send({difference});
});

// 9 - Query Parameters
app.get('/multiplication', (req, res) => {
    const num1 = parseFloat(req.query.num1);
    const num2 = parseFloat(req.query.num2);

    const product = num1 * num2;
    res.status(200).send({product});
});

// 10 - Headers
app.get('/wordlength', (req, res) => {
    const word = req.headers['x-word'];

    const length = word.length;
    res.status(200).send({length});
});






app.listen(PORT, (error) => {
    if (!error) {
        console.error(`Server is running on http://localhost:${PORT}`);
    } else {
        console.log(`Error occured, server can't start`, error);
    }
});