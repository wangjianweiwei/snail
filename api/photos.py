import os
from PIL import Image
from uuid import uuid4
from typing_extensions import List, Self
from datetime import datetime

from pydantic import BaseModel
from fastapi import APIRouter, UploadFile, Form, Depends

from util import Token
from config import settings
from models.photos import Events, Photos

router = APIRouter()


class EventSchema(BaseModel):
    id: int
    title: str
    count: int
    created_at: str

    @staticmethod
    def format_datetime(dt: datetime) -> str:
        return dt.strftime('%Y.%m.%d %H:%M:%S')  # 自定义时间格式

    @classmethod
    def from_orm(cls, event: Events) -> Self:
        return cls(id=event.id,
                   count=event.count,
                   title=event.title,
                   created_at=cls.format_datetime(event.created_at))


class PhotosSchema(BaseModel):
    id: int
    original: str
    thumbnail: str
    created_at: str

    @staticmethod
    def format_datetime(dt: datetime) -> str:
        return dt.strftime('%Y.%m.%d %H:%M:%S')  # 自定义时间格式

    @staticmethod
    def format_path(path: str) -> str:
        return f"{settings.SERVER_NAME}/{path}"

    @classmethod
    def from_orm(cls, photos: Photos) -> Self:
        return cls(id=photos.id,
                   original=cls.format_path(photos.original),
                   thumbnail=cls.format_path(photos.thumbnail),
                   created_at=cls.format_datetime(photos.created_at))


def generate_thumbnail(input_path, output_path):
    try:
        # 打开原图
        with Image.open(input_path) as img:
            # 保持原比例生成缩略图
            img.thumbnail((350.0, 350.0))
            # 保存缩略图
            img.save(output_path)
            print(f"缩略图已保存到: {output_path}")
    except Exception as e:
        print(f"生成缩略图时发生错误: {e}")


@router.post("/")
async def upload(images: List[UploadFile], name: str = Form(), user=Depends(Token.user)):
    event, _ = await Events.get_or_create(title=name)

    photos = []
    for image in images:
        uuid = uuid4().hex
        original_path = os.path.join(settings.ORIGINAL_PATH, f"{uuid}_{image.filename}")
        with open(original_path, "wb") as f:
            f.write(image.file.read())

        thumbnail_path = os.path.join(settings.THUMBNAIL_PATH, f"{uuid}_thumbnail_{image.filename}")
        generate_thumbnail(original_path, thumbnail_path)
        photo = Photos(thumbnail=thumbnail_path, original=original_path, event=event)
        photos.append(photo)
        event.count += 1

    await Photos.bulk_create(photos)
    await event.save()

    return {
        "data": None,
        "status": True,
        "msg": None
    }


@router.get("/")
async def list_images(user=Depends(Token.user)):
    values = ["id", "thumbnail", "original", "created_at"]
    photos = await Photos.filter().values(*values)

    return {
        "data": [PhotosSchema.from_orm(Photos(**photo)) for photo in photos],
        "status": True,
        "msg": None
    }


@router.get("/events")
async def events():
    queryset = await Events.filter()

    return {
        "data": [EventSchema.from_orm(event) for event in queryset],
        "status": True,
        "msg": None
    }
