import bcrypt

from tortoise import fields, Model  # noqa


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255, unique=True, null=True)
    salt = fields.BinaryField(null=True)  # 存储盐
    avatar_url = fields.CharField(max_length=255, null=True)
    password_hash = fields.BinaryField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    otp_code = fields.CharField(max_length=32, unique=True)

    def set_password(self, password: str) -> None:
        self.salt = bcrypt.gensalt(14)
        self.password_hash = bcrypt.hashpw(password.encode(), self.salt)


class ThirdPartyAuth(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='third_party_auths', on_delete=fields.CASCADE)  # 关联User
    provider = fields.CharField(max_length=50)  # 第三方平台名称 (如 'github', 'wechat', 'google' 等)
    provider_user_id = fields.CharField(max_length=255, unique=True)  # 第三方平台的唯一用户ID
    access_token = fields.CharField(max_length=255, null=True)  # 授权的访问Token
    avatar_url = fields.CharField(max_length=255, null=True)  # 用户的头像URL
    created_at = fields.DatetimeField(auto_now_add=True)  # 绑定时间
    updated_at = fields.DatetimeField(auto_now=True)  # 更新时间

    class Meta:
        table = "third_party_auth"
        unique_together = (('provider', 'provider_user_id'),)  # 保证provider和provider_user_id唯一
