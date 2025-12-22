from pydantic import BaseModel, Field
from src.books.schemas import BookModel
from src.reviews.schemas import ReviewModel
from datetime import datetime
from typing import List
import uuid

class UserCreateModel(BaseModel):  #Remember this schemas are serialization and our models are storage(main)
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    username: str = Field(max_length=10)
    email: str = Field(max_length=40)
    password: str = Field(min_length=8)


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime
    updated_at: datetime


class UserBooksModel(UserModel):
    books: List[BookModel]
    reviews: List[ReviewModel]


class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=8, max_length=72)
