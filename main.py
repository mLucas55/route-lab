from fastapi import FastAPI
from pydantic import BaseModel

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
                "10. CRASH THE APP SERVER ---- /byebye"
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
        print("Fork Crashing the server... Fork count:", counter)