"""Pydantic schemas for request/response validation."""

from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    """Schema para criar um usuario."""

    username: str
    email: Optional[EmailStr] = None


class UserRead(BaseModel):
    """Schema para ler/devolver um usuario."""

    id: int
    username: str
    email: Optional[str] = None

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    """Schema para atualizar um usuario."""

    username: Optional[str] = None
    email: Optional[str] = None
