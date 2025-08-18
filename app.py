from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from ext import startup
from api import auth
from api import posts
from api import todo
from api import photos
from api import rag

snail = FastAPI(lifespan=startup)
snail.mount("/images", StaticFiles(directory="images"), name="images")

snail.add_middleware(
    CORSMiddleware,  # noqa
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

snail.include_router(auth.router, prefix="/api/auth")
snail.include_router(posts.router, prefix="/api/posts")
snail.include_router(todo.router, prefix="/api/todo")
snail.include_router(photos.router, prefix="/api/photos")
snail.include_router(rag.router, prefix="/api/rag")
