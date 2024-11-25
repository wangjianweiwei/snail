from tortoise import fields, Model  # noqa


class Posts(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=64, default="未命名")
    content = fields.JSONField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    abstract = fields.CharField(max_length=128)
    status = fields.SmallIntField(default=0)
    wordcount = fields.IntField(default=0)
