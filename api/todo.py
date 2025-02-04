from math import ceil

from fastapi import APIRouter, Body
from pydantic import BaseModel

from datetime import datetime
from models.todo import TodoItem, Category

router = APIRouter()


class CategorySchema(BaseModel):
    id: int
    name: str
    children: list = []


@router.get("/")
async def query(page: int = 1, size: int = 20, status: str = None, date: str = None):
    if status == "1":
        if date:
            start = f"{date} {datetime.min.time()}"
            end = f"{date} {datetime.max.time()}"
            todos = TodoItem.filter(is_completed=True, completed_at__gte=start, completed_at__lt=end)
        else:
            todos = TodoItem.filter(is_completed=True)
    elif status == "0":
        if date:
            todos = TodoItem.filter(is_completed=False, plan_at=date)
        else:
            todos = TodoItem.filter(is_completed=False)
    else:
        todos = TodoItem.filter()

    count = await todos.count()
    result = await todos.order_by("created_at").offset((page - 1) * size).limit(size)

    return {
        "data": {"count": count, "paged": result, "page_count": ceil(count / size)},
        "status": True,
        "msg": None
    }


@router.post("/create")
async def create(title: str = Body(embed=True)):
    todo = await TodoItem.create(title=title)

    return {
        "data": todo,
        "status": True,
        "msg": None
    }


@router.delete("/delete")
async def delete(pk: int):
    await TodoItem.filter(pk=pk).delete()
    return {
        "data": None,
        "status": True,
        "msg": None
    }


@router.put("/update")
async def update(pk: int = Body(embed=True), updated: dict = Body()):
    if updated.get("is_completed"):
        updated["completed_at"] = datetime.now()

    await TodoItem.filter(pk=pk).update(**updated)
    return {
        "data": None,
        "status": True,
        "msg": None
    }


@router.get("/category")
async def category(parent: int = None):
    objects = await Category.filter(parent_id=parent).values("id", "name")

    return {
        "data": [CategorySchema(**n) for n in objects],
        "status": True,
        "msg": None
    }


@router.post("/category/create")
async def category(name: str, parent: int = None):
    obj = Category(parent_id=parent, name=name)
    await obj.save()

    return {
        "data": obj,
        "status": True,
        "msg": None
    }
