"""Uvicorn server runner."""

import uvicorn


def run():
    """Run the FastAPI server."""
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    run()
