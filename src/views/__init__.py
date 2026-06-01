from src.views.auth_view import (
    EmailModel,
    PasswordResetConfirmModel,
    PasswordResetRequestModel,
    UserCreateModel,
    UserLoginModel,
)
from src.views.book_view import Book, BookCreateModel, BookDetailModel, BookUpdateModel
from src.views.review_view import ReviewCreateModel, ReviewModel
from src.views.tag_view import TagAddModel, TagCreateModel, TagModel
from src.views.user_view import UserBooksModel, UserModel

__all__ = [
    "Book",
    "BookCreateModel",
    "BookDetailModel",
    "BookUpdateModel",
    "EmailModel",
    "PasswordResetConfirmModel",
    "PasswordResetRequestModel",
    "ReviewCreateModel",
    "ReviewModel",
    "TagAddModel",
    "TagCreateModel",
    "TagModel",
    "UserBooksModel",
    "UserCreateModel",
    "UserLoginModel",
    "UserModel",
]
