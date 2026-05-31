"""User database model using SQLAlchemy Core."""

from sqlalchemy import Table, Column, Integer, String
from app.database.connection import metadata

User = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(255), nullable=False, index=True),
    Column("email", String(255), nullable=True),
)
