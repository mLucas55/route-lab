# Introduction

A containerizable FastAPI backend with 12 different interactive routes for Cloud Computing Lab-4.

# Description

This project is a FastAPI-based web application, expected to run on a Uvicorn app server with the option to containerize it in docker. Consiting of 12 routes, this "application" offers a range of functionality, from simple tasks like string storage to more advanced features such as IP-based location lookup via an external API, response-headers, and cookie reading.

# Design

The project is designed using FastAPI for its efficiency and modernity. Eeach route is modular and clearly defined for simplicity, I.E. one route saves strings and another route displays saved strings. An environment variable is used for the IP-based location lookup route, a free key can be obtained at https://ipstack.com

The provided Dockerfile allows this FastAPI app to be built as an image and ran in a container.


Route and input structure:

1. INDEX -------------------- /
2. RETURNS A PROVIDED AGE --- /age_query?age={age}
3. SAVE A STRING ------------ /save_string/{string}
4. DISPLAY SAVED STRINGS ---- /display_strings
5. THE CURRENT TIME --------- /time
6. IP AND LOCATION INFO ----- /your_location/{ip_address}
7. ADDITION ----------------- /plus/{a}/{b}
8. SUBTRACTION -------------- /minus/{a}/{b}
9. GENERATE A RANDOM WORD --- /random_word
10. CRASH THE APP SERVER ---- /byebye
11. HEADERS DEMO ------------ /headers
12. COOKIE DEMO ------------- /session_cookie

# Running The Application (Browser)

1. Clone this repo to your local machine
2. Reference the requirements.txt file to make sure all dependencies are installed
3. Open a terminal in the working directory.
4. In the terminal, type: "uvicorn main:app --port 8080" (optionally include "--reload" for hot refresh)
5. Run the command
6. Open the generated URL

# Running The Application (CLI Driver)

1. Clone this repo to your local machine
2. Reference the requirements.txt file to make sure all dependencies are installed
3. Open a terminal in the working directory.
4. In the terminal, type: "uvicorn main:app --port 8080" (optionally include "--reload" for hot refresh)
5. Run the command
6. Run driver.py

# Running The Application (Container)

1. Clone this repo to your local machine
2. In terminal run: docker build -t <name>
3. In terminal run: docker run -p 8080:8080 <name>
4. View the container using the Docker desktop app and UI

# Running Examples

Launching The Server and Viewing Activity:
<img width="812" alt="Server Running" src="https://github.com/user-attachments/assets/4bd03ac4-00cf-4039-99c2-f580936bbb3e" />

Index Page:
<img width="1512" alt="Index Page" src="https://github.com/user-attachments/assets/a22edd0a-5a9c-4b11-b9db-b4d66c925785" />

Example of IP-based Location Lookup:
<img width="1512" alt="Your Location" src="https://github.com/user-attachments/assets/0dc956f3-6e4a-43f6-a7bd-411eaf8cc86d" />





