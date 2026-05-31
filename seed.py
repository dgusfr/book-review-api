"""Seed script to populate initial test data."""

import asyncio
import sys
from pathlib import Path

# Add app to path
sys.path.insert(0, str(Path(__file__).parent))

from app.database.connection import create_tables, database
from app.services.user_service import UserService


async def seed_data():
    """Insert initial test users into the database."""
    await create_tables()
    await database.connect()

    users_data = [
        {"username": "João", "email": "joao@example.com"},
        {"username": "Maria", "email": "maria@example.com"},
        {"username": "Pedro", "email": "pedro@example.com"},
    ]

    try:
        for user in users_data:
            await UserService.create_user(user["username"], user["email"])
        print(f"✓ {len(users_data)} usuários inseridos com sucesso.")
    finally:
        await database.disconnect()


if __name__ == "__main__":
    asyncio.run(seed_data())
