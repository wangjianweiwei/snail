from typing import Any, Optional
from datetime import datetime, timedelta

from tortoise.fields import DatetimeField as BaseDatetimeField
from jwt.exceptions import PyJWTError
from jwt.api_jwt import decode as jwt_decode, encode as jwt_encode

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class Token:

    def __init__(self, token):
        self.token = token
        self.__payload = None
        self.__user = None

    @classmethod
    def create(cls, user: dict, expires: timedelta = None) -> "Token":
        if expires:
            expire = datetime.utcnow() + expires
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        user.update({"exp": expire})
        token = cls(token=jwt_encode(user, SECRET_KEY, algorithm="HS256"))
        token.__payload = user

        return token

    @classmethod
    def validate(cls, token: str) -> "Token":
        try:
            payload = jwt_decode(token, SECRET_KEY, algorithms=["HS256"])
            o = cls(token=token)
            o.__payload = payload

            return o
        except PyJWTError as e:
            raise Exception("Invalid token") from e

    @classmethod
    def user(cls, token: str):
        token = cls.validate(token)
        pk = token.__payload.get("pk")

        return pk


class PasswordAuth:

    def auth(self):
        raise NotImplemented


class GithubAuth(PasswordAuth):

    def auth(self):
        token = Token.create()

        return token.token


class DatetimeField(BaseDatetimeField):

    def __init__(self, auto_now: bool = False, auto_now_add: bool = False, format="%Y-%m-%d %H:%M:%S", **kwargs: Any, ):
        self.format = format
        super().__init__(auto_now, auto_now_add, **kwargs)

    def to_python_value(self, value: Any) -> Optional[datetime]:
        return super().to_python_value(value)
