"""Database access helpers (thin layer).

Keep query functions small and focused so the web layer can call them
and transform results as needed.
"""

from typing import Dict, List

from src.database import USERS, database


async def get_all_users() -> List[Dict]:
    """Fetch all users from the `users` table.

    Steps:
    1. Build a SELECT query using the `USERS` table object.
    2. Execute the query using the shared `database` connection.
    3. Convert each returned row to a plain dict so HTTP layer can serialize it.
    """

    # 1) Build the query
    query = USERS.select()

    # 2) Execute query (returns list of Row objects)
    rows = await database.fetch_all(query)

    # 3) Convert rows to simple dictionaries.
    #    With SQLAlchemy/Databases versions, rows expose data via `_mapping`.
    users: List[Dict] = []
    for row in rows:
        mapping = getattr(row, "_mapping", row)
        users.append(dict(mapping))

    return users
