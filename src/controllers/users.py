from model.repository.users_repository import UsersRepository


class UsersController:
    """Controller layer for user-related operations."""

    def __init__(self):
        self.__users_repository = UsersRepository()

    async def list_users(self) -> list:
        users = await self.__users_repository.get_all_users()

        list_users = []
        for user in users:
            list_users.append(
                {
                    "id": user["id"],
                    "username": user["username"],
                }
            )

        return list_users
