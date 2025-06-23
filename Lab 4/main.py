from fastapi import FastAPI, Response, Cookie, Header
from pydantic import BaseModel
from typing import Optional

from dotenv import load_dotenv
import os

from datetime import datetime
import requests
from random_word import RandomWords

app = FastAPI()

ip_api_key = os.getenv("API_KEY")

saved_strings = []

#1 - Index
@app.get("/")
async def read_root():
    return {"Routes": [
                "1. INDEX -------------------- /",
                "2. RETURNS A PROVIDED AGE --- /age_query?age={age}",
                "3. SAVE A STRING ------------ /save_string/{string}",
                "4. DISPLAY SAVED STRINGS ---- /display_strings",
                "5. THE CURRENT TIME --------- /time",
                "6. IP AND LOCATION INFO ----- /your_location/{ip_address}",
                "7. ADDITION ----------------- /plus/{a}/{b}",
                "8. SUBTRACTION -------------- /minus/{a}/{b}",
                "9. GENERATE A RANDOM WORD --- /random_word",
                "10. CRASH THE APP SERVER ---- /byebye",
                "11. HEADERS DEMO ------------ /hello_headers",
                "12. COOKIE DEMO ------------- /read_cookie"
            ]}

#2 - Age (query parameter)
@app.get("/age_query")
async def hello_path(age: int):
    return {"message": f"You are {age} years old!"}

#3 - Save a string
@app.get("/save_string/{string}")
async def save_string(string: str):
    saved_strings.append(string)
    return {"Appended": {string}}

#4
@app.get("/display_strings")
async def display_strings():
    return {"Saved strings": saved_strings}

#5 - Current date and time
@app.get("/time")
async def time():
    now = datetime.now()
    formatted = now.strftime('%Y-%m-%d %H:%M')
    return {"Date and time": formatted}

#6 - Location info
@app.get("/your_location/{ip_address}")
async def your_location(ip_address: str):
    url = f"https://api.ipstack.com/{ip_address}?access_key={ip_api_key}"
    response = requests.get(url)
    data = response.json()
    return {"IP Info": data}

#7 - plus
@app.get("/plus/{a}/{b}")
async def plus(a: int, b: int):
   result = a + b
   return {"Result": result}
        
#8 - Minus
@app.get("/minus/{a}/{b}")
async def plus(a: int, b: int):
   result = a - b
   return {"Result": result}

#9 - Random word
@app.get("/random_word")
async def random_word():
    r = RandomWords()
    return {"Random word": r.get_random_word()}

#10 - Crash Uvicorn
@app.get("/byebye")
async def byebye():
    counter = 0
    while True:
        os.fork
        counter+= 1
        print("Crashing the server... Fork count:", counter)

#11 - HEADERS
@app.get("/headers")
async def hello_headers(name: Optional[str] = Header(None)):
    print("Received header:", name)
    return {"Header-name": name}
    
#12 - Cookie
@app.get("/session_cookie")
async def read_cookie(response: Response, session_id: Optional[str] = Cookie(None)):
    if session_id:
        return {"session_id": session_id}
    else:
        new_session_id = "session_123"
        response.set_cookie(key="session_id", value=new_session_id)
        return {"message": "Session cookie set.", "session_id": new_session_id}