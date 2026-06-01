from fastapi import FastAPI

from src.controllers import auth_router, book_router, review_router, tags_router
from src.core.exception_handlers import register_all_errors
from src.core.middleware import register_middleware


version = "v1"
version_prefix = f"/api/{version}"

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service.",
    version=version,
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
)

register_all_errors(app)
register_middleware(app)

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"{version_prefix}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"{version_prefix}/tags", tags=["tags"])


@app.get("/", tags=["health"])
async def root() -> dict[str, str]:
    return {"message": "Welcome to Bookly API"}


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
