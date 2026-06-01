import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ReviewModel(BaseModel):
    uid: uuid.UUID
    rating: int = Field(lt=5)
    review_text: str
    user_uid: Optional[uuid.UUID] = None
    book_uid: Optional[uuid.UUID] = None
    created_at: datetime
    update_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ReviewCreateModel(BaseModel):
    rating: int = Field(lt=5)
    review_text: str
