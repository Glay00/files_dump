from fastapi import applications

from . import dump


def include_routers(app: applications.FastAPI) -> None:
    app.include_router(dump.router, tags=["test"])
