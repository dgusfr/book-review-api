import logging

from fastapi import status
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.repositories.review_repository import ReviewRepository
from src.core.services.book_service import BookService
from src.core.services.user_service import UserService
from src.models.review_model import Review
from src.views.review_view import ReviewCreateModel


class ReviewService:
    def __init__(
        self,
        review_repository: ReviewRepository | None = None,
        book_service: BookService | None = None,
        user_service: UserService | None = None,
    ) -> None:
        self.review_repository = review_repository or ReviewRepository()
        self.book_service = book_service or BookService()
        self.user_service = user_service or UserService()

    async def add_review_to_book(
        self,
        user_email: str,
        book_uid: str,
        review_data: ReviewCreateModel,
        session: AsyncSession,
    ):
        try:
            book = await self.book_service.get_book(book_uid=book_uid, session=session)
            user = await self.user_service.get_user_by_email(
                email=user_email,
                session=session,
            )

            if not book:
                raise HTTPException(
                    detail="Book not found",
                    status_code=status.HTTP_404_NOT_FOUND,
                )

            if not user:
                raise HTTPException(
                    detail="User not found",
                    status_code=status.HTTP_404_NOT_FOUND,
                )

            review_data_dict = review_data.model_dump()
            new_review = Review(**review_data_dict, user=user, book=book)

            return await self.review_repository.create(new_review, session)

        except HTTPException:
            raise
        except Exception as exc:
            logging.exception(exc)
            raise HTTPException(
                detail="Oops... something went wrong!",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    async def get_review(self, review_uid: str, session: AsyncSession):
        return await self.review_repository.get_by_uid(review_uid, session)

    async def get_all_reviews(self, session: AsyncSession):
        return await self.review_repository.get_all(session)

    async def delete_review_to_from_book(
        self,
        review_uid: str,
        user_email: str,
        session: AsyncSession,
    ):
        user = await self.user_service.get_user_by_email(user_email, session)
        review = await self.get_review(review_uid, session)

        if not review or review.user != user:
            raise HTTPException(
                detail="Cannot delete this review",
                status_code=status.HTTP_403_FORBIDDEN,
            )

        await self.review_repository.delete(review, session)
