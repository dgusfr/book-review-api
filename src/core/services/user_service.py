from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.repositories.user_repository import UserRepository
from src.core.security.password import generate_passwd_hash
from src.models.user_model import User
from src.views.auth_view import UserCreateModel


class UserService:
    def __init__(self, user_repository: UserRepository | None = None) -> None:
        self.user_repository = user_repository or UserRepository()

    async def get_user_by_email(self, email: str, session: AsyncSession):
        return await self.user_repository.get_by_email(email, session)

    async def user_exists(self, email: str, session: AsyncSession) -> bool:
        user = await self.get_user_by_email(email, session)
        return user is not None

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(
            username=user_data_dict["username"],
            email=user_data_dict["email"],
            first_name=user_data_dict["first_name"],
            last_name=user_data_dict["last_name"],
            password_hash=generate_passwd_hash(user_data_dict["password"]),
            role="user",
        )

        return await self.user_repository.create(new_user, session)

    async def update_user(
        self,
        user: User,
        user_data: dict,
        session: AsyncSession,
    ):
        return await self.user_repository.update(user, user_data, session)
