"""Lightweight entry point to run the API server directly."""
from .api import app


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
