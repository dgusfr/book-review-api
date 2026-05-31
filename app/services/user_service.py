"""User service with business logic."""

from typing import Dict, List, Optional

from app.database.connection import database
from app.models.user import User


class UserService:
    """Service layer for user operations."""

    @staticmethod
    async def get_all_users() -> List[Dict]:
        """Fetch all users from database."""
        query = User.select()
        result = await database.fetch_all(query)
        return [dict(r) for r in result]

    @staticmethod
    async def get_user_by_id(user_id: int) -> Optional[Dict]:
        """Fetch a single user by ID."""
        query = User.select().where(User.c.id == user_id)
        result = await database.fetch_one(query)
        return dict(result) if result else None

    @staticmethod
    async def create_user(username: str, email: Optional[str] = None) -> Dict:
        """Create a new user."""
        query = User.insert().values(username=username, email=email)
        last_record_id = await database.execute(query)
        return {"id": last_record_id, "username": username, "email": email}

    @staticmethod
    async def update_user(
        user_id: int, username: Optional[str] = None, email: Optional[str] = None
    ) -> Optional[Dict]:
        """Update an existing user."""
        values = {}
        if username is not None:
            values["username"] = username
        if email is not None:
            values["email"] = email

        if not values:
            return await UserService.get_user_by_id(user_id)

        query = User.update().where(User.c.id == user_id).values(**values)
        await database.execute(query)
        return await UserService.get_user_by_id(user_id)

    @staticmethod
    async def delete_user(user_id: int) -> bool:
        """Delete a user by ID."""
        query = User.delete().where(User.c.id == user_id)
        result = await database.execute(query)
        return result > 0
