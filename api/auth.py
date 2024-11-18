# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/9/28 08:07
"""
import base64
from io import BytesIO
from datetime import timedelta

import aiohttp
import pyotp
import qrcode
from fastapi import APIRouter, Depends, Body
from models.auth import User
from util import Token

router = APIRouter()


# @router.post("/login")
async def register_github(code: str = Body(embed=True)):
    data = {
        "code": code,
        "client_id": "17f2d31fca5f88282646",
        "client_secret": "81af6b088094f1fa70e1e1697ef6cd6a0926f938",
    }
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post("https://github.com/login/oauth/access_token", data=data, ssl=False,
                                headers=headers) as response:
            data = await response.json()
            access_token = data.get("access_token")

        headers = {
            "Authorization": f"token {access_token}",
            "Accept": "application/json"
        }
        async with session.get("https://api.github.com/user", headers=headers, ssl=False) as response:
            userinfo = await response.json()
        defaults = {
            "username": userinfo["name"],
            "avatar_url": userinfo["avatar_url"],

        }
        user, created = await User.get_or_create(defaults=defaults, id=userinfo["id"])

        return user


@router.post("/register")
async def register(email: str = Body(embed=True), secret: str = Body(embed=True)):
    user, created = await User.get_or_create(defaults={"username": email, "otp_code": secret}, email=email)
    if not created:
        return {
            "data": None,
            "status": False,
            "msg": "该账号已经存在"
        }

    return {
        "data": None,
        "status": True,
        "msg": "账号创建成功"
    }


@router.post("/login")
async def login(email: str = Body(embed=True), otp_code: str = Body(embed=True)):
    user = await User.get_or_none(email=email).values("id", "username", "email", "otp_code", "avatar_url")
    if not user:
        return {
            "data": None,
            "status": False,
            "msg": "账号不存在"
        }

    otp = pyotp.TOTP(user["otp_code"])
    if not otp.verify(otp_code):
        return {
            "data": None,
            "status": False,
            "msg": "登陆失败"
        }

    token = Token.create(user, expires=timedelta(weeks=4))
    return {
        "data": {
            "user": user,
            "token": token.token
        },
        "status": True,
        "msg": "登陆成功"
    }


@router.get("/otp_qrcode")
async def create_otp_qrcode(email: str):
    secret = pyotp.random_base32(32)

    otp = pyotp.TOTP(secret)
    url = otp.provisioning_uri(email, issuer_name="discuss.pub")
    image = qrcode.make(url)
    bytesio = BytesIO()
    image.save(bytesio, format="PNG")

    img_base64 = base64.b64encode(bytesio.getvalue()).decode("utf-8")

    return {
        "data": {
            "secret": secret,
            "qrcode": img_base64
        },
        "status": True,
        "msg": None
    }
