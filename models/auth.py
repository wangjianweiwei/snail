from tortoise import fields, Model  # noqa


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=32, unique=True)
    password = fields.CharField(max_length=64)
