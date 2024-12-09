import os
from PIL import Image
from uuid import uuid4
from typing import List, Any, Self
from datetime import datetime

from pydantic import BaseModel
from fastapi import APIRouter, UploadFile, Form

from models.photos import Events, Photos

router = APIRouter()
O_PATH = "images"
T_PATH = "images"


class PhotosSchema(BaseModel):
    id: int
    original: str
    thumbnail: str
    created_at: str

    @staticmethod
    def format_datetime(dt: datetime) -> str:
        return dt.strftime('%Y.%m.%d  %H:%M:%S')  # 自定义时间格式

    @staticmethod
    def format_path(path: str) -> str:
        # return f"http://127.0.0.1:8000/{path}"
        return f"http://me-api.ifmatch.top/{path}"

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
            # 确保输出目录存在

            # 保存缩略图
            img.save(output_path)
            print(f"缩略图已保存到: {output_path}")
    except Exception as e:
        print(f"生成缩略图时发生错误: {e}")


@router.post("/")
async def upload(images: List[UploadFile], name: str = Form()):
    event, _ = await Events.get_or_create(title=name)

    photos = []
    for image in images:
        uuid = uuid4().hex
        o_path = os.path.join(O_PATH, f"{uuid}_{image.filename}")
        with open(o_path, "wb") as f:
            f.write(image.file.read())

        t_path = os.path.join(O_PATH, f"{uuid}_thumbnail_{image.filename}")
        generate_thumbnail(o_path, t_path)
        photo = Photos(thumbnail=t_path, original=o_path, event=event)
        photos.append(photo)

    await Photos.bulk_create(photos)

    return {
        "success": True
    }


@router.get("/")
async def list_images():
    values = ["id", "thumbnail", "original", "created_at"]
    photos = await Photos.filter().values(*values)

    return {
        "data": [PhotosSchema.from_orm(Photos(**photo)) for photo in photos],
        "status": True,
        "msg": None
    }
