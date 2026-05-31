"""User controller handling request logic."""

from typing import List

from src.schemas.user_schema import UserCreate, UserRead, UserUpdate
from src.services.user_service import UserService


class UserController:
    """Controller layer for user operations."""

    @staticmethod
    async def list_users() -> List[UserRead]:
        """Get all users."""
        users = await UserService.get_all_users()
        return [UserRead(**user) for user in users]

    @staticmethod
    async def get_user(user_id: int) -> UserRead:
        """Get a user by ID."""
        user = await UserService.get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        return UserRead(**user)

    @staticmethod
    async def create_user(user_data: UserCreate) -> UserRead:
        """Create a new user."""
        new_user = await UserService.create_user(username=user_data.username, email=user_data.email)
        return UserRead(**new_user)

    @staticmethod
    async def update_user(user_id: int, user_data: UserUpdate) -> UserRead:
        """Update an existing user."""
        updated_user = await UserService.update_user(user_id, user_data.username, user_data.email)
        if not updated_user:
            raise ValueError(f"User {user_id} not found")
        return UserRead(**updated_user)

    @staticmethod
    async def delete_user(user_id: int) -> bool:
        """Delete a user."""
        deleted = await UserService.delete_user(user_id)
        if not deleted:
            raise ValueError(f"User {user_id} not found")
        return True
