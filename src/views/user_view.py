import uuid
from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field

from src.views.book_view import Book
from src.views.review_view import ReviewModel


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime
    update_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserBooksModel(UserModel):
    books: List[Book] = []
    reviews: List[ReviewModel] = []
