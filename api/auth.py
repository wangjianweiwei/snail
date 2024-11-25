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


@router.post("/register")
async def register(email: str = Body(embed=True), secret: str = Body(embed=True)):
    exists = await User.exists()
    if exists:
        return {
            "data": None,
            "status": False,
            "msg": "系统已经初始化"
        }
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


@router.get("/check_initialization")
async def check_initialization():
    exists = await User.exists()

    return {
        "data": exists,
        "status": True,
        "msg": None
    }
