from fastapi import FastAPI
from pydantic import BaseModel

from datetime import datetime
import requests

app = FastAPI()

#1
@app.get("/")
async def read_root():
    return {"message": "Routes to try",
            "routes": [
                "1 - /"
                "2- /hello",
                "3- /hello_path/{name}/{age}",
                "4- hello_personclass",
                "5- /time",
                "6- your_location/{ip_address}",
            ]}

#2
@app.get("/hello")
async def hello(name: str, age: int):
    return {"message": f"Hello {name}, you are {age} years old!"}

#3
@app.get("/hello_path/{name}/{age}")
async def hello_path(name: str, age: int):
    return {"message": f"Hello {name}, you are {age} years old!"}

class PersonInput(BaseModel):
    name: str
    age: int

#4 - Self documenting and validating
@app.post("/hello_personclass")
async def hello_personclass(input: PersonInput):
    return f"Hello {input.name}, you are {input.age} years old!"

#5
@app.get("/time")
async def time():
    now = datetime.now()
    formatted = now.strftime('%Y-%m-%d %H:%M')
    return {"Date and time": formatted}

#6
@app.get("/your_location/{ip_address}")
async def your_location(ip_address: str):
    url = f"https://api.ipstack.com/{ip_address}?access_key=62fbb4a2e0359346047c8f5b96e0fea1"
    response = requests.get(url)
    data = response.json()
    return {"IP Info": data}

