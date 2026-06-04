from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.book_model import Book


class BookRepository:
    async def get_all(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_by_user_uid(self, user_uid: str, session: AsyncSession):
        statement = (
            select(Book)
            .where(Book.user_uid == user_uid)
            .order_by(desc(Book.created_at))
        )
        result = await session.exec(statement)
        return result.all()

    async def get_by_uid(self, book_uid: str, session: AsyncSession) -> Book | None:
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement)
        return result.first()

    async def create(self, book: Book, session: AsyncSession) -> Book:
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book

    async def update(
        self, book: Book, update_data: dict, session: AsyncSession
    ) -> Book:
        for key, value in update_data.items():
            setattr(book, key, value)

        await session.commit()
        await session.refresh(book)
        return book

    async def delete(self, book: Book, session: AsyncSession) -> None:
        await session.delete(book)
        await session.commit()
