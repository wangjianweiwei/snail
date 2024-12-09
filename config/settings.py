import os

from config import Const


class Setting:
    env = 'DEFAULT'
    debug = True
    host = 'localhost'
    port = 8000
    log_level = 'DEBUG'

    tortoise_orm = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.mysql",  # 数据库引擎 Mysql or Mariadb
                "credentials": {
                    "host": "127.0.0.1",
                    "port": "3306",
                    "user": "root",
                    "password": "123456",
                    "database": "snail",
                    "minsize": 1,
                    "maxsize": 5,
                    "charset": "utf8mb4",
                    "echo": True
                }
            }
        },
        "apps": {
            "models": {
                "models": ["models.auth", "models.posts", "models.todo", "models.photos", "aerich.models"],
                "default_connection": "default",
            },
        },
        "timezone": 'Asia/Shanghai'
    }


class DevelopmentSetting(Setting):
    env = 'DEVELOPMENT'


class TestingSetting(Setting):
    env = "TESTING"
    log_level = 'INFO'


class ProductionSetting(Setting):
    env = "PRODUCTION"
    host = "0.0.0.0"
    log_level = 'ERROR'

    tortoise_orm = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.mysql",  # 数据库引擎 Mysql or Mariadb
                "credentials": {
                    "host": "8.152.160.172",
                    "port": "3306",
                    "user": "root",
                    "password": "TPvg5xI@",
                    "database": "snail-prod",
                    "minsize": 1,
                    "maxsize": 5,
                    "charset": "utf8mb4",
                    "echo": True
                }
            }
        },
        "apps": {
            "models": {
                "models": ["models.auth", "models.posts", "models.todo", "models.photos", "aerich.models"],
                "default_connection": "default",
            },
        },
        "timezone": "Asia/Shanghai"
    }


settings = {
    Setting.env: Setting,
    DevelopmentSetting.env: DevelopmentSetting,
    TestingSetting.env: TestingSetting,
    ProductionSetting.env: ProductionSetting
}

env = os.environ.get(Const.SNAIL_ENV_KEY)
setting = settings.get(env, DevelopmentSetting)()
