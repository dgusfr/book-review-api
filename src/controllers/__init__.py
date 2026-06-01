from src.controllers.auth_controller import auth_router
from src.controllers.book_controller import book_router
from src.controllers.review_controller import review_router
from src.controllers.tag_controller import tags_router

__all__ = [
    "auth_router",
    "book_router",
    "review_router",
    "tags_router",
]
