from tortoise import fields, Model  # noqa


class Events(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=64, null=False)
    count = fields.IntField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class Photos(Model):
    id = fields.IntField(pk=True)
    thumbnail = fields.CharField(max_length=256, null=False)
    original = fields.CharField(max_length=256, null=False)
    event = fields.ForeignKeyField("models.Events", related_name="photos")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
