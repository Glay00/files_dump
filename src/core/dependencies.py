from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    A coroutine that asynchronously yields an AsyncSession object.
    """

    from src.app import sessionmaker

    async with sessionmaker() as session:
        yield session
