from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.db.connection import create_tables, database
from src.controllers.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure DB tables exist (development)
    create_tables()

    # Connect shared async database
    await database.connect()
    try:
        yield
    finally:
        await database.disconnect()


app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(users_router, prefix="/users", tags=["users"])


@app.get("/")
async def root():
    return JSONResponse(content={"message": "Hello from src app"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
