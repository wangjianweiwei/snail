from uvicorn import run

from app import snail
from config import setting

if __name__ == '__main__':
    run(snail, host=setting.host, port=setting.port)
