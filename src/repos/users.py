from typing import List, Dict

from src.db.connection import USERS, database


async def get_all_users() -> List[Dict]:
    """Return all users as plain dictionaries."""
    query = USERS.select()
    rows = await database.fetch_all(query)

    users: List[Dict] = []
    for row in rows:
        mapping = getattr(row, "_mapping", row)
        users.append(dict(mapping))

    return users
