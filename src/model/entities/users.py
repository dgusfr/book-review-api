from sqlalchemy import Column, Integer, String, Table

from src.model.settings.db_metadata import MetaData

Users = Table(
    "users",
    MetaData(),
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String),
)
