uvicorn main:app --port 8080 --reload

https://ipstack.com/dashboard



Notes:

Have to use async methods in routes because uvicorn is an async app server









@app.get("/hello")
async def hello(name: str, age: int):
    return {"message": f"Hello {name}, you are {age} years old!"}

Query Paramters: ? + &
http://localhost:8080/hello?name=Lucas&age=22