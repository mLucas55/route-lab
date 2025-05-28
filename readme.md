# Introduction

A FastAPI backend with 10 different interactive routes for Cloud Computing Lab-1.

# Description

This project is a FastAPI-based web application, expected to run on a Uvicorn app server. Consiting of 10 routes, this "application" offers a range of functionality, from simple tasks like string storage to more advanced features such as IP-based location lookup via an external API.

# Design

The project is designed using FastAPI for its efficiency and modernity. Eeach route is modular and clearly defined for simplicity, I.E. one route saves strings and another route displays saved strings. An environment variable is used for the IP-based location lookup route, a free key can be obtained at https://ipstack.com


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


# Running The Application

1. Clone this repo to your local machine
2. Reference the requirements.txt file to make sure all dependencies are installed
3. Open a terminal in the working directory.
4. In the terminal, type: "uvicorn main:app --port 8080" (optionally include "--reload" for hot refresh)
5. Run the command
6. Open the generated URL

# Running Examples

Launching the server and viewing activity:
<img width="812" alt="Server Running" src="https://github.com/user-attachments/assets/4bd03ac4-00cf-4039-99c2-f580936bbb3e" />

Index Page:
<img width="1512" alt="Index Page" src="https://github.com/user-attachments/assets/a22edd0a-5a9c-4b11-b9db-b4d66c925785" />

Example of IP-based location lookup:
<img width="1512" alt="Your Location" src="https://github.com/user-attachments/assets/0dc956f3-6e4a-43f6-a7bd-411eaf8cc86d" />





