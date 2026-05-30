"""Database connection and table definitions.

This module centralizes the database connection so other modules
can import `database` and the table objects (e.g. `USERS`).

Why separate file:
- Keeps connection logic in one place for clarity
- Allows the web app to connect/disconnect in a single place
"""

from pathlib import Path

import databases
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.engine import Engine

# 1) Database URL
#    Use absolute path so API and DBeaver point to the same sqlite file.
BASE_DIR = Path(__file__).resolve().parent
SQLITE_FILE = BASE_DIR / "schema.db"
DATABASE_URL = f"sqlite:///{SQLITE_FILE}"

# 2) `database` is the async Database object used by the app to execute queries
database = databases.Database(DATABASE_URL)

# 3) SQLAlchemy metadata and table definitions (schema)
metadata = MetaData()

USERS = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(255), nullable=False),
)

# 4) Synchronous engine used only for creating tables during setup
engine: Engine = create_engine(DATABASE_URL)


def create_tables() -> None:
    """Create database tables if they don't exist.

    Run this once during development or as part of a deploy/migration step.
    Example:
        python -c 'from database import create_tables; create_tables()'
    """
    metadata.create_all(engine)
