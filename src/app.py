from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqladmin import Admin
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.api import include_routers
from src.controller import controller as base_controller
from src.core.config.settings import setup_config

config = setup_config()
engine = create_async_engine(config.db.dsn)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None]:
    """
    An async context manager function that manages the lifespan of the FastAPI application.
    Args:
        _app (FastAPI): The FastAPI instance.
    Returns:
        AsyncGenerator[None]: An async generator that yields control back.
    """

    async with engine.begin(), AsyncSession(engine) as session:
        base_controller.base_controller = base_controller.BaseController(session)
        yield


app = FastAPI(title="FastAPI Starter", lifespan=lifespan)
include_routers(app)

# Administration settings
admin_panel = Admin(app, engine=engine)
