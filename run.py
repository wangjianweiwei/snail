from uvicorn import run

from app import snail
from config import settings

if __name__ == '__main__':
    run(snail, host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
