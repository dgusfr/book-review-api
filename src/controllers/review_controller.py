from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.database import get_session
from src.core.dependencies import get_current_user
from src.core.security.permissions import RoleChecker
from src.core.services.review_service import ReviewService
from src.models.user_model import User
from src.views.review_view import ReviewCreateModel, ReviewModel

review_router = APIRouter()

review_service = ReviewService()

admin_role_checker = Depends(RoleChecker(["admin"]))
user_role_checker = Depends(RoleChecker(["user", "admin"]))


@review_router.get(
    "/",
    response_model=List[ReviewModel],
    dependencies=[admin_role_checker],
)
async def get_all_reviews(
    session: AsyncSession = Depends(get_session),
):
    reviews = await review_service.get_all_reviews(session)

    return reviews


@review_router.get(
    "/{review_uid}",
    response_model=ReviewModel,
    dependencies=[user_role_checker],
)
async def get_review(
    review_uid: str,
    session: AsyncSession = Depends(get_session),
):
    review = await review_service.get_review(review_uid, session)

    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found",
        )

    return review


@review_router.post(
    "/book/{book_uid}",
    response_model=ReviewModel,
    status_code=status.HTTP_201_CREATED,
    dependencies=[user_role_checker],
)
async def add_review_to_books(
    book_uid: str,
    review_data: ReviewCreateModel,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    new_review = await review_service.add_review_to_book(
        user_email=current_user.email,
        review_data=review_data,
        book_uid=book_uid,
        session=session,
    )

    return new_review


@review_router.delete(
    "/{review_uid}",
    dependencies=[user_role_checker],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_review(
    review_uid: str,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    await review_service.delete_review_to_from_book(
        review_uid=review_uid,
        user_email=current_user.email,
        session=session,
    )

    return None
