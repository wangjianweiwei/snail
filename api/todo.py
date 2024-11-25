from fastapi import APIRouter, Body

from datetime import datetime
from models.todo import TodoItem

router = APIRouter()


@router.get("/")
async def query(status: str = None, date: str = None):
    if status == "1":
        todos = TodoItem.filter(is_completed=True)
    elif status == "0":
        todos = TodoItem.filter(is_completed=False)
    else:
        todos = TodoItem.filter()

    if date:
        date = datetime.strptime(date, "%Y-%m-%d")
        if status == "1":
            todos = todos.filter(completed_at__year=date.year,
                                 completed_at__month=date.month,
                                 completed_at__day=date.day)
        if status == "0":
            todos = todos.filter(plan_at=date)

    result = await todos.order_by("created_at")

    return {
        "data": {"count": 0, "paged": result, "page_count": 0},
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
async def delete(pk: int = Body(embed=True), updated: dict = Body()):
    print(updated)
    await TodoItem.filter(pk=pk).update(**updated)
    return {
        "data": None,
        "status": True,
        "msg": None
    }
