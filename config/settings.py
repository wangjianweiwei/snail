from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB_NAME: str
    MYSQL_CHARSET: str = "utf8mb4"
    MODELS: list = ["models.auth", "models.posts", "models.todo", "models.photos", "aerich.models"]

    HOST: str = "localhost"
    PORT: int = 8000
    DEBUG: bool = False

    TIMEZONE: str = "Asia/Shanghai"

    THUMBNAIL_PATH: str = "images"
    ORIGINAL_PATH: str = "images"

    SERVER_NAME: str = "http://127.0.0.1:8000"

    class Config:
        env_file = ".env"


settings = Settings()
