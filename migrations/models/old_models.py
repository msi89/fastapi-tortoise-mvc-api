from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=60, default=None, null=True)
    username = fields.CharField(max_length=25, unique=True)
    email = fields.CharField(max_length=256, unique=True)
    password = fields.CharField(max_length=1000)
    is_admin = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
    avatar = fields.CharField(max_length=256, default=None, null=True)

    def __str__(self):
        return f"{self.name} {self.email}"

    async def save(self, *args, **kwargs) -> None:
        self.password = "123456"
        await super().save(*args, **kwargs)

    class PydanticMeta:
        exclude = ['password']
from tortoise.models import Model
from tortoise import fields


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    body = fields.TextField()
    image = fields.CharField(max_length=250)
    author = fields.ForeignKeyField(
        'diff_models.User', related_name='author', on_delete='CASCADE')
    created = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.title
from tortoise import Model, fields

MAX_VERSION_LENGTH = 255


class Aerich(Model):
    version = fields.CharField(max_length=MAX_VERSION_LENGTH)
    app = fields.CharField(max_length=20)

    class Meta:
        ordering = ["-id"]
