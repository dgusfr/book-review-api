"""FastAPI application setup."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.connection import database, create_tables
from app.routes.user_routes import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for app startup and shutdown."""
    # Startup
    create_tables()
    await database.connect()
    yield
    # Shutdown
    await database.disconnect()


app = FastAPI(
    title="User API",
    description="A simple user management API",
    version="1.0.0",
    lifespan=lifespan,
)

# Include routers
app.include_router(user_router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to User API"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
