"""

This module make connection to the database and create tables if they don't exist.
"""

from databases import Database


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///./schema.db"
        self.__database = Database(self.__connection_string)

    async def connect(self):
        await self.__database.connect()

    async def disconnect(self):
        await self.__database.disconnect()

    def get_database(self) -> Database:
        return self.__database


db_connection_handler = DBConnectionHandler()
