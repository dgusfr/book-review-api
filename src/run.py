import asyncio

from model.repository.users_repository import UsersRepository
from model.settings.db_connection_handler import db_connection_handler


async def main():
    await db_connection_handler.connect()

    users_repository = UsersRepository()
    users = await users_repository.get_all_users()

    for user in users:
        print(user.name)

    await db_connection_handler.disconnect()


asyncio.run(main())
