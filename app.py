from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ext import startup
from api import auth

snail = FastAPI(lifespan=startup)

snail.add_middleware(
    CORSMiddleware,  # noqa
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

snail.include_router(auth.router, prefix="/api/auth")
