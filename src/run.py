import asyncio

from controllers.users import UsersController
from model.settings.db_connection_handler import db_connection_handler


async def main():
    await db_connection_handler.connect()

    users_controller = UsersController()
    users = await users_controller.list_users()

    if not users:
        print("Nenhum usuario encontrado.")
    else:
        for user in users:
            print(user)

    await db_connection_handler.disconnect()


asyncio.run(main())
