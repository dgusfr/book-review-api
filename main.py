import asyncio

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    await asyncio.sleep(2)  # Simulando uma operação assíncrona
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet_name(name: str, age: int) -> dict:
    return {"message": f"Hello, {name}! You are {age} years old."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
