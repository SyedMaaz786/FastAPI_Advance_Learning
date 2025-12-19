from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class UserCreateModel(BaseModel):  #Remember this schemas are serialization and our models are storage(main)
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    username: str = Field(max_length=10)
    email: str = Field(max_length=40)
    password: str = Field(min_length=8, max_length=72)


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


class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=8, max_length=72)
