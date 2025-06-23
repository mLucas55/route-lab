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

1. Clone this repo to your local machine (VSCode recommended)
2. Establish a Python environment (venv recommended)
3. Reference the requirements.txt file to make sure all dependencies are installed - https://ipstack.com
4. If intending to use route 6 (ip and location info) make sure to obtain an API key
5. Open a terminal in the working directory
6. In the terminal, type: "uvicorn main:app --port 8080" (optionally include "--reload" for hot refresh)
7. Run the command
8. Open the generated URL

# Running The Application (CLI Driver)

1. Clone this repo to your local machine (VSCode recommended)
2. Establish a Python environment (venv recommended)
3. Reference the requirements.txt file to make sure all dependencies are installed - https://ipstack.com
4. If intending to use route 6 (ip and location info) make sure to obtain an API key
5. Open a terminal in the working directory
6. In the terminal type and run: "uvicorn main:app --port 8080" (optionally include "--reload" for hot refresh)
7. In the terminal type and run : "python driver.py"

# Running The Application (Container)

1. Clone this repo to your local machine (VSCode recommended)
2. Obtain an API key for route 6 (IP Info) - https://ipstack.com
3. Enter the API key into the Dockerfile "ENV" line
4. Open a terminal in the working directory
5. In terminal type and run: docker build -t <name>
6. In terminal type and run: docker run -p 8080:8080 <name>
7. Verify the container was succesfuly created (Docker desktop app/ui recommended)
8. Interact with the routes using terminal in the working directory (Docker desktop app/ui recommended)
