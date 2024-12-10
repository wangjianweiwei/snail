from config import settings

TORTOISE_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",  # 数据库引擎 Mysql or Mariadb
            "credentials": {
                "host": settings.MYSQL_HOST,
                "port": settings.MYSQL_PORT,
                "user": settings.MYSQL_USER,
                "password": settings.MYSQL_PASSWORD,
                "database": settings.MYSQL_DB_NAME,
                "minsize": 1,
                "maxsize": 5,
                "charset": settings.MYSQL_CHARSET,
            }
        }
    },
    "apps": {
        "models": {
            "models": settings.MODELS,
            "default_connection": "default",
        },
    },
    "timezone": settings.TIMEZONE
}
