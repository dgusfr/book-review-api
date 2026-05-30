"""DB connection used by the application (async).

This centralizes the database URL and `database` object so the rest
of the app can import it from a single place.
"""

from pathlib import Path

import databases
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.engine import Engine

# Base project directory (two levels up from this file: project root)
BASE_DIR = Path(__file__).resolve().parents[2]
SQLITE_FILE = BASE_DIR / "schema.db"
DATABASE_URL = f"sqlite:///{SQLITE_FILE}"

# Async database object used by `databases` package
database = databases.Database(DATABASE_URL)

# SQLAlchemy metadata and table definitions
metadata = MetaData()

USERS = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(255), nullable=False),
)

# Synchronous engine for schema creation
engine: Engine = create_engine(DATABASE_URL)


def create_tables() -> None:
    """Create tables if missing (development convenience)."""
    metadata.create_all(engine)
