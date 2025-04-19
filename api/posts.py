import os
import math
from uuid import uuid4
from config import settings
from typing import Any
from datetime import datetime
from typing_extensions import Self

from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Body, File, UploadFile, Depends, Header

from util import Token
from models.posts import Posts

router = APIRouter()


class PostSchema(BaseModel):
    id: int
    title: str
    created_at: str
    abstract: str
    wordcount: int
    published: bool
    content: Any = None

    @staticmethod
    def format_datetime(dt: datetime) -> str:
        return dt.strftime('%Y.%m.%d  %H:%M:%S')  # 自定义时间格式

    @classmethod
    def from_orm(cls, post: Posts) -> Self:
        return cls(id=post.id, title=post.title, created_at=cls.format_datetime(post.created_at),
                   abstract=post.abstract, content=post.content, wordcount=post.wordcount, published=post.published)


@router.get("/")
async def query(page: int, size: int, token: str = Header(default=None)):
    """
    列表页

    :return:
    """
    print(token)
    if token is not None:
        try:
            Token.validate(token)
            posts = Posts.filter(status=1)
        except HTTPException:
            print("1111")
            posts = Posts.filter(published=1)
    else:
        posts = Posts.filter(published=1)

    count = await posts.count()
    values = ("id", "title", "created_at", "abstract", "wordcount", "published")
    paged = await posts.order_by("-created_at").offset((page - 1) * size).limit(size).values(*values)
    return {
        "data": {"count": count,
                 "paged": [PostSchema.from_orm(Posts(**post)) for post in paged],
                 "page_count": math.ceil(count / size or 1)},
        "status": True,
        "msg": None
    }


@router.get("/retrieve")
async def retrieve(pk: int):
    """

    :return:
    """
    post = await Posts.filter(pk=pk).first()

    return {
        "data": PostSchema.from_orm(post),
        "status": True,
        "msg": None
    }


@router.put("/update")
async def update(pk: int = Body(embed=True), title: str = Body(embed=True), user=Depends(Token.user)):
    """
    更新

    :return:
    """
    await Posts.filter(pk=pk).update(title=title)

    return {
        "data": None,
        "status": True,
        "msg": None
    }


@router.delete("/destroy")
async def destroy(pk: int = Body(embed=True), user=Depends(Token.user)):
    """
    删除

    :param pk:
    :param user:
    :return:
    """
    await Posts.filter(pk=pk).update(status=0, published=False)

    return {
        "data": None,
        "status": True,
        "msg": None
    }


@router.post("/create")
async def create(title: str = Body(embed=True), user=Depends(Token.user)):
    """
    创建

    :return:
    """
    post = Posts(title=title, content=None, abstract="", status=1)
    await post.save()
    return {
        "data": post,
        "status": True,
        "msg": None
    }


@router.put("/compose")
async def compose(
        content: dict = Body(embed=True),
        pk: int = Body(embed=True),
        abstract: str = Body(embed=True),
        wordcount: int = Body(embed=True),
        user=Depends(Token.user)):
    """
    保存

    :return:
    """
    await Posts.filter(pk=pk).update(content=content, abstract=abstract, wordcount=wordcount)
    return {
        "data": True,
        "status": True,
        "msg": None
    }


@router.post("/publish")
async def publish(pk: int = Body(embed=True), published: bool = Body(embed=True), user=Depends(Token.user)):
    """
    发布

    :return:
    """
    await Posts.filter(pk=pk).update(published=published)
    return {
        "data": None,
        "status": True,
        "msg": None
    }


@router.post("/image/upload")
async def image_upload(image: UploadFile):
    """
    上传图片

    :return:
    """
    filename = f"{uuid4().hex}_{image.filename}"
    original_path = os.path.join(settings.ORIGINAL_PATH, filename)

    with open(original_path, "wb") as f:
        f.write(image.file.read())

    return {
        "data": {
            "url": f"{settings.SERVER_NAME}/{original_path}",
            "size": image.size,
            "filename": filename
        },
        "status": True,
        "msg": None
    }

# @router.post("/image/signature")
# async def image_signature(pk: int = Body(embed=True), path: str = Body(embed=True)):
#     """
#     图片签名
#
#     :return:
#     """
