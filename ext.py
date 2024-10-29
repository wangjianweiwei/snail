from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise  # noqa

from config import setting


async def init_db() -> None:
    await Tortoise.init(setting.tortoise_orm)


@asynccontextmanager
async def startup(app: FastAPI):
    print("start")
    await init_db()
    yield
    print("shutdown")
