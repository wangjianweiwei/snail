import math

from delta import Delta
from fastapi import APIRouter, Body, File, UploadFile

from models.posts import Posts

router = APIRouter()


@router.get("/")
async def query(page: int, size: int):
    """
    列表页

    :return:
    """
    posts = Posts.filter(status=1)
    count = await posts.count()
    paged = await posts.order_by("-created_at").offset((page - 1) * size).limit(size)

    return {
        "data": {"count": count, "paged": paged, "page_count": math.ceil(count / size or 1)},
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
        "data": post,
        "status": True,
        "msg": None
    }


@router.put("/update")
async def update(pk: int = Body(embed=True), title: str = Body(embed=True)):
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
async def destroy(pk: int = Body(embed=True)):
    """
    删除

    :param pk:
    :return:
    """
    await Posts.filter(pk=pk).delete()

    return {
        "data": None,
        "status": True,
        "msg": None
    }


@router.post("/create")
async def create(title: str = Body(embed=True)):
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
async def compose(content: dict = Body(embed=True), pk: int = Body(embed=True)):
    """
    保存

    :return:
    """
    snapshot = Delta(content["ops"])
    abstract = snapshot.document()[:128]
    await Posts.filter(pk=pk).update(content=content, abstract=abstract)
    return {
        "data": None,
        "status": True,
        "msg": None
    }


@router.get("/publish")
async def publish(pk: int):
    """
    发布

    :return:
    """
    await Posts.filter(pk=pk).update(status=1)
    return {
        "data": None,
        "status": True,
        "msg": None
    }


# @router.post("/image/upload")
# async def image_upload(image: Body(embed=True), pk: int = Body()):
#     """
#     上传图片
#
#     :return:
#     """

# @router.post("/image/signature")
# async def image_signature(pk: int = Body(embed=True), path: str = Body(embed=True)):
#     """
#     图片签名
#
#     :return:
#     """
