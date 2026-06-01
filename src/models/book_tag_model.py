from __future__ import annotations

import uuid

from sqlmodel import Field, SQLModel


class BookTag(SQLModel, table=True):
    __tablename__ = "booktag"

    book_id: uuid.UUID = Field(
        default=None,
        foreign_key="books.uid",
        primary_key=True,
    )
    tag_id: uuid.UUID = Field(
        default=None,
        foreign_key="tags.uid",
        primary_key=True,
    )
