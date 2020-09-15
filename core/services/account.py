
from core.models.accounts import User
from tortoise.contrib.pydantic import pydantic_model_creator
from core.schemas.accounts import UserSchema

model = pydantic_model_creator(User)


class AccountService():

    async def list():
        return await model.from_queryset(User.all())

    async def create(user: UserSchema):
        user_obj = await User.create(**user.dict())
        return model.from_orm(user_obj)

    async def login():
        pass
