from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.review_model import Review


class ReviewRepository:
    async def get_all(self, session: AsyncSession):
        statement = select(Review).order_by(desc(Review.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_by_uid(self, review_uid: str, session: AsyncSession) -> Review | None:
        statement = select(Review).where(Review.uid == review_uid)
        result = await session.exec(statement)
        return result.first()

    async def create(self, review: Review, session: AsyncSession) -> Review:
        session.add(review)
        await session.commit()
        await session.refresh(review)
        return review

    async def delete(self, review: Review, session: AsyncSession) -> None:
        await session.delete(review)
        await session.commit()
