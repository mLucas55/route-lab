# Introduction

A FastAPI backend with 10 different interactive routes for Cloud Computing Lab-1.

# Description

This project is a FastAPI-based web application, expected to run on a Uvicorn app server. Consiting of 10 routes, each route besides the index is interactive, some using queary parameters, and most using paths. These routes offer a range of functionality, from simple tasks like string storage to more advanced features such as IP-based location lookup via an external API.

# Design

There are 10 routes with the following input structure:
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



uvicorn main:app --port 8080 --reload




https://ipstack.com/dashboard
