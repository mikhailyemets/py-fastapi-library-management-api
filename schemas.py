from datetime import datetime
from pydantic import BaseModel
from typing import List


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: datetime
    author_id: int


class BookCreate(BookBase):
    author_id: int


class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: List[Book] = []

    class Config:
        orm_mode = True
