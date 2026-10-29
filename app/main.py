from fastapi import FastAPI

from app import __version__
from app.api import health, v1


def create_app() -> FastAPI:
    app = FastAPI(title="flexable-ai", version=__version__)
    app.include_router(health.router)
    app.include_router(v1.router)
    return app


app = create_app()
