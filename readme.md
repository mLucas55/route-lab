uvicorn main:app --port 8080 --reload

https://ipstack.com/dashboard



Notes:

Have to use async methods in routes because uvicorn is an async app server

Query Paramters: ? + &
http://localhost:8080/hello?name=Lucas&age=22