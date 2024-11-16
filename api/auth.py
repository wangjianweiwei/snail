# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/9/28 08:07
"""
import email

import aiohttp
from fastapi import APIRouter, Depends, Body
from models.auth import User

router = APIRouter()


@router.post("/login")
async def register(code: str = Body(embed=True)):
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
