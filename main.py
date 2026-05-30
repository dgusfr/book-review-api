"""
This file is the HTTP layer. It should:
- import small, focused DB helpers from `run.py` (or similar)
- use a lifespan handler to connect/disconnect the shared DB
- keep route handlers thin and focused on input/output transformations
"""

import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.database import create_tables, database
from src.run import get_all_users


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan handler: connects to DB on startup and disconnects on shutdown.

    FastAPI previously used `@app.on_event("startup")` and `shutdown`, but
    the current recommended approach is to pass a `lifespan` async contextmanager
    to `FastAPI(...)`.
    """

    # 1) Ensure tables exist before serving requests
    create_tables()

    # 2) Connect to the shared async database
    await database.connect()
    try:
        # 3) Yield control to let the app start and serve requests
        yield
    finally:
        # 4) Ensure we always disconnect when the app stops
        await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    await asyncio.sleep(2)  # Simulando uma operação assíncrona
    return {"message": "Hello World"}


@app.get("/users")
async def read_users() -> JSONResponse:
    """Route to return all users in a JSON-friendly format.

    Step-by-step:
    1) Call the DB helper `get_all_users()` which returns list[dict].
    2) Transform the DB field names to the API field names (e.g. `name` -> `username`).
    3) Return a `Response` with a JSON string body and `application/json` media type.
    """

    # 1) Fetch raw user rows from DB helper
    users = await get_all_users()

    # 2) Transform rows to the response shape.
    #    The DB column is already `username`, so we keep it explicit here.
    transformed = [{"id": u.get("id"), "username": u.get("username")} for u in users]

    # 3) Return the final JSON payload using `JSONResponse` which handles
    #    JSON encoding and content type automatically.
    payload = {"users": transformed}
    return JSONResponse(content=payload)


if __name__ == "__main__":
    # Importing `uvicorn` here keeps the module import fast when used as ASGI
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
