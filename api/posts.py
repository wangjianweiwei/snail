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
    paged = await posts.order_by(Posts.created_at.desc()).offset((page - 1) * size).limit(size).values()

    return {
        "data": {"count": count, "paged": paged, "page": page, "size": size},
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
async def update(pk: int = Body(embed=True)):
    """
    更新

    :return:
    """
    await Posts.filter(pk=pk).update(title="斯蒂芬森地方")

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
async def create(
        title: str = Body(embed=True),
        content: str = Body(embed=True)
):
    """
    创建

    :return:
    """
    post = Posts(title=title, content=content, abstract="123123")
    await post.save()
    return {
        "data": post.title,
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


@router.post("/image/upload")
async def image_upload(file: UploadFile = File(), pk: int = Body()):
    """
    上传图片

    :return:
    """


@router.post("/image/signature")
async def image_signature(pk: int = Body(embed=True), path: str = Body(embed=True)):
    """
    图片签名

    :return:
    """
