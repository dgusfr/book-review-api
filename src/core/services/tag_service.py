from fastapi import status
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.exceptions import BookNotFound, TagAlreadyExists, TagNotFound
from src.core.repositories.tag_repository import TagRepository
from src.core.services.book_service import BookService
from src.models.tag_model import Tag
from src.views.tag_view import TagAddModel, TagCreateModel


class TagService:
    def __init__(
        self,
        tag_repository: TagRepository | None = None,
        book_service: BookService | None = None,
    ) -> None:
        self.tag_repository = tag_repository or TagRepository()
        self.book_service = book_service or BookService()

    async def get_tags(self, session: AsyncSession):
        """Get all tags."""
        return await self.tag_repository.get_all(session)

    async def add_tags_to_book(
        self,
        book_uid: str,
        tag_data: TagAddModel,
        session: AsyncSession,
    ):
        """Add tags to a book."""
        book = await self.book_service.get_book(book_uid=book_uid, session=session)

        if not book:
            raise BookNotFound()

        for tag_item in tag_data.tags:
            tag = await self.tag_repository.get_by_name(tag_item.name, session)

            if not tag:
                tag = Tag(name=tag_item.name)

            book.tags.append(tag)

        session.add(book)
        await session.commit()
        await session.refresh(book)

        return book

    async def get_tag_by_uid(self, tag_uid: str, session: AsyncSession):
        """Get tag by uid."""
        return await self.tag_repository.get_by_uid(tag_uid, session)

    async def add_tag(self, tag_data: TagCreateModel, session: AsyncSession):
        """Create a tag."""
        tag = await self.tag_repository.get_by_name(tag_data.name, session)

        if tag:
            raise TagAlreadyExists()

        new_tag = Tag(name=tag_data.name)
        return await self.tag_repository.create(new_tag, session)

    async def update_tag(
        self,
        tag_uid: str,
        tag_update_data: TagCreateModel,
        session: AsyncSession,
    ):
        """Update a tag."""
        tag = await self.get_tag_by_uid(tag_uid, session)

        if not tag:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        update_data_dict = tag_update_data.model_dump()
        return await self.tag_repository.update(tag, update_data_dict, session)

    async def delete_tag(self, tag_uid: str, session: AsyncSession):
        """Delete a tag."""
        tag = await self.get_tag_by_uid(tag_uid, session)

        if not tag:
            raise TagNotFound()

        await self.tag_repository.delete(tag, session)
