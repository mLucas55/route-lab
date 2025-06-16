# Introduction

A Express.js backend with 10 different interactive routes for Cloud Computing Lab-3.

# Description

This project is a Express.js web application, expected to be tested with Postman. Consiting of 10 routes, this "application" offers a range of functionality, from simple tasks like addition to more advanced features such as payment processing.

# Design

The project is designed using Express.js and node. Eeach route is modular and clearly defined for simplicity. Routes take information via either query parameters or headers and return either HTML content or a JSON response.


Route and input structure:

1. ABOUT -------------------- /about
2. HELLO NAME --------------- /helloname?name={name}
3. FAVORITE NUMBER ---------- /favoritenumber?number={number}
4. INVENTORY ITEM ----------- /inventory?item={itemId}
5. PROCESS PAYMENT ---------- /processpayment (POST)
6. GUESS THE NUMBER --------- /guessTheNumber?number={number}
7. ADDITION ----------------- /addition?num1={num1}&num2={num2}
8. SUBTRACTION -------------- /subtraction (uses headers x-num1, x-num2)
9. MULTIPLICATION ----------- /multiplication?num1={num1}&num2={num2}
10. WORD LENGTH ------------- /wordlength (uses header x-word)

# Running The Application (Browser)

1. Clone this repo to your local machine
2. Reference the requirements.txt file to make sure all dependencies are installed
3. Open a terminal in the working directory.
4. In the terminal, type: "node main.js"
5. Copy the URL and paste it into Postman
5. Begin using its routes!

# Running The Application (CLI Driver)

1. Clone this repo to your local machine
2. Reference the requirements.txt file to make sure all dependencies are installed
3. Open a terminal in the working directory.
4. In the terminal, type: "uvicorn main:app --port 8080" (optionally include "--reload" for hot refresh)
5. Run the command
6. Run driver.py




