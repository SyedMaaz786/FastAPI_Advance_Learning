from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English"
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "publisher": "Addison-Wesley",
        "published_date": "1999-10-20",
        "page_count": 352,
        "language": "English"
    },
    {
        "id": 3,
        "title": "You Don't Know JS",
        "author": "Kyle Simpson",
        "publisher": "O'Reilly Media",
        "published_date": "2015-12-27",
        "page_count": 278,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "publisher": "MIT Press",
        "published_date": "2009-07-31",
        "page_count": 1312,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_count": 544,
        "language": "English"
    },
    {
        "id": 6,
        "title": "Design Patterns",
        "author": "Erich Gamma",
        "publisher": "Addison-Wesley",
        "published_date": "1994-10-31",
        "page_count": 395,
        "language": "English"
    }
]

class BookModel(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str 
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    publisher: str
    page_count: int
    language: str

#GET
@app.get("/books", response_model = List[BookModel])
async def get_all_books():
    return books

#POST
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: BookModel) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get("/books/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book 
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Book not found")

#UPDATE
@app.patch("/books/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 

#DELETE
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")