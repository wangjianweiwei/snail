# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/11/18 17:56
"""
from tortoise import fields, Model  # noqa


class TodoItem(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, blank=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    is_completed = fields.BooleanField(default=False)
    completed_at = fields.DatetimeField(null=True, blank=True)
    plan_at = fields.DateField(null=True, blank=True, db_index=True)
    priority = fields.SmallIntField(default=100, db_index=True)


class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, blank=False, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    parent = fields.ForeignKeyField("models.Category", related_name="children", null=True)