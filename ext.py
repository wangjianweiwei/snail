from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise  # noqa

from config.aerich import TORTOISE_CONFIG


async def init_db() -> None:
    await Tortoise.init(TORTOISE_CONFIG)


@asynccontextmanager
async def startup(app: FastAPI):
    print("start")
    await init_db()
    yield
    print("shutdown")
