from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Optional

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from src.models.book_model import Book
    from src.models.user_model import User


class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4,
        )
    )
    rating: int = Field(lt=5)
    review_text: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False)
    )
    user_uid: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="users.uid",
    )
    book_uid: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="books.uid",
    )
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now)
    )
    update_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now)
    )

    user: Optional["User"] = Relationship(back_populates="reviews")
    book: Optional["Book"] = Relationship(back_populates="reviews")

    def __repr__(self) -> str:
        return f"<Review {self.uid}>"
