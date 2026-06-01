from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.user_model import User


class UserRepository:
    async def get_by_email(self, email: str, session: AsyncSession) -> User | None:
        statement = select(User).where(User.email == email)
        result = await session.exec(statement)
        return result.first()

    async def create(self, user: User, session: AsyncSession) -> User:
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    async def update(self, user: User, user_data: dict, session: AsyncSession) -> User:
        for key, value in user_data.items():
            setattr(user, key, value)

        await session.commit()
        await session.refresh(user)
        return user
