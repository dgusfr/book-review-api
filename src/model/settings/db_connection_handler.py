"""Database connection handler.

This module connects to SQLite and creates tables from the shared SQLAlchemy metadata.
"""

from pathlib import Path

from databases import Database
from sqlalchemy import create_engine

from model.settings.db_metadata import metadata


class DBConnectionHandler:
    def __init__(self) -> None:
        base_dir = Path(__file__).resolve().parents[2]
        sqlite_file = base_dir / "schema.db"
        self.__connection_string = f"sqlite:///{sqlite_file}"
        self.__database = Database(self.__connection_string)
        self.__engine = create_engine(self.__connection_string)

    async def connect(self):
        metadata.create_all(self.__engine)
        await self.__database.connect()

    async def disconnect(self):
        await self.__database.disconnect()

    def get_database(self) -> Database:
        return self.__database


db_connection_handler = DBConnectionHandler()
