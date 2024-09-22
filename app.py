from fastapi import FastAPI

from config import setting
from ext import startup

snail = FastAPI(lifespan=startup)
