from datetime import datetime
from uuid import UUID

from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.repositories.book_repository import BookRepository
from src.models.book_model import Book
from src.views.book_view import BookCreateModel, BookUpdateModel


class BookService:
    def __init__(self, book_repository: BookRepository | None = None) -> None:
        self.book_repository = book_repository or BookRepository()

    async def get_all_books(self, session: AsyncSession):
        return await self.book_repository.get_all(session)

    async def get_user_books(self, user_uid: str, session: AsyncSession):
        return await self.book_repository.get_by_user_uid(user_uid, session)

    async def get_book(self, book_uid: str, session: AsyncSession):
        return await self.book_repository.get_by_uid(book_uid, session)

    async def create_book(
        self,
        book_data: BookCreateModel,
        user_uid: str,
        session: AsyncSession,
    ):
        book_data_dict = book_data.model_dump()

        new_book = Book(**book_data_dict)
        new_book.published_date = datetime.strptime(
            book_data_dict["published_date"],
            "%Y-%m-%d",
        ).date()
        new_book.user_uid = UUID(str(user_uid))

        return await self.book_repository.create(new_book, session)

    async def update_book(
        self,
        book_uid: str,
        update_data: BookUpdateModel,
        session: AsyncSession,
    ):
        book_to_update = await self.get_book(book_uid, session)

        if book_to_update is None:
            return None

        update_data_dict = update_data.model_dump()
        return await self.book_repository.update(
            book_to_update,
            update_data_dict,
            session,
        )

    async def delete_book(self, book_uid: str, session: AsyncSession):
        book_to_delete = await self.get_book(book_uid, session)

        if book_to_delete is None:
            return None

        await self.book_repository.delete(book_to_delete, session)
        return {}
