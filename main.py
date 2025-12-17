from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello There! This is Syed Maaz."}


@app.get("/greet/{name}")      # Here we have created a route which takes input from the url itself and prints it in the result page
async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:        
    return {"message": f"Welcome {name}", "age": age}     # This is the example of path and Query parameter

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }
