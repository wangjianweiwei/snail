# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/9/28 08:07
"""

from fastapi import APIRouter, Depends

from util import GithubAuth

router = APIRouter()


@router.get("/register")
async def register(username: str, password: str):
    return {"hrll": ""}


@router.get("/login/password")
async def login_password(username: str, password: str):
    return {"hrll": ""}


@router.get("/login/github")
async def login_github(username: str, password: str):
    return {"hrll": ""}


@router.get("/github/callback")
async def github_callback():
    GithubAuth.auth()


@router.get("/userinfo")
async def user_info(token):
    pass
