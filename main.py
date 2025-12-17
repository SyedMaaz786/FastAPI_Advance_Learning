from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello There! This is Syed Maaz."}


@app.get("/greet/{name}")      # Here we have created a route which takes input from the url itself and prints it in the result page
async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:        
    return {"message": f"Welcome {name}", "age": age}     # This is the example of path and Query parameter

class BookCreateModel(BaseModel):  #Created a model which consists of what type of data our req takes
    title: str
    author: str

@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }

@app.get("/get_headers", status_code=222)   #Getting header info
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
):
    
    request_header = {}

    request_header["Accept"] = accept              #reading the value and storing in the key value pair, check GPT if not able to recall.
    request_header["Content-Type"] = content_type
    request_header["User-Agent"] = user_agent
    request_header["Host"] = host

    return request_header
