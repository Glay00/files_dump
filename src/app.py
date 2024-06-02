from fastapi import FastAPI

from src.api import include_routers

app = FastAPI(title="FastAPI Starter")
include_routers(app)
