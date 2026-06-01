import uuid
from datetime import date, datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from src.views.review_view import ReviewModel
from src.views.tag_view import TagModel


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    update_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BookDetailModel(Book):
    reviews: List[ReviewModel] = []
    tags: List[TagModel] = []


class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
