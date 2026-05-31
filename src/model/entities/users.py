from sqlalchemy import Column, Integer, String, Table

from model.settings.db_metadata import metadata

Users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
)
