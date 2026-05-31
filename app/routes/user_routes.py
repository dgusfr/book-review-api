"""User API routes."""

from typing import List

from fastapi import APIRouter, HTTPException

from app.controllers.user_controller import UserController
from app.schemas.user_schema import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserRead])
async def list_users():
    """List all users."""
    return await UserController.list_users()


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int):
    """Get a user by ID."""
    try:
        return await UserController.get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=UserRead)
async def create_user(user_data: UserCreate):
    """Create a new user."""
    return await UserController.create_user(user_data)


@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user_data: UserUpdate):
    """Update an existing user."""
    try:
        return await UserController.update_user(user_id, user_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """Delete a user."""
    try:
        await UserController.delete_user(user_id)
        return {"detail": f"User {user_id} deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
