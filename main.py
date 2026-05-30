import asyncio
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    await asyncio.sleep(2)  # Simulando uma operação assíncrona
    return {"message": "Hello World"}


@app.get("/greet")
async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Hello, {name}! You are {age} years old."}


class BookCreateMOdel(BaseModel):
    title: str
    author: str


@app.post("/create_book")
async def create_book(book: BookCreateMOdel):
    return {"title": book.title, "author": book.author}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
