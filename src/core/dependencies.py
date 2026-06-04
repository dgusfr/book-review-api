from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.database import get_session
from src.core.security.jwt import AccessTokenBearer
from src.core.services.user_service import UserService

user_service = UserService()


async def get_current_user(
    token_details: dict = Depends(AccessTokenBearer()),
    session: AsyncSession = Depends(get_session),
):
    user_email = token_details["user"]["email"]
    user = await user_service.get_user_by_email(user_email, session)
    return user
