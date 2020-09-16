
from core.models.accounts import User
from tortoise.contrib.pydantic import pydantic_model_creator
from core.schemas.accounts import UserSchema, UserUpdateSchema
from core.middlewares.auth import (
    authenticate, create_access_token, change_user_password, get_current_active_user)
from core.middlewares.security import hash_password, verify_password
from core.exceptions import raise_authenticate

model = pydantic_model_creator(User)


class AccountService():

    async def get(id: int = None):
        if(id is not None):
            return await model.from_queryset_single(User.get(id=id))
        return await model.from_queryset(User.all())

    async def create(user: UserSchema):
        user_obj = await User.create(**user.dict())
        return model.from_orm(user_obj)

    async def update(id: int, user: UserUpdateSchema):
        await User.filter(id=id).update(**user.dict(exclude_unset=True))
        return await model.from_queryset_single(User.get(id=id))

    async def sign_in(email: str, password: str):
        user = await authenticate(email, password)
        if not user:
            return raise_authenticate()
        token = create_access_token(data=user.__dict__)
        return {"access_token": token, "meta": model.from_orm(user)}

    async def reset_user_password(id: int, password: str) -> User:
        await User.filter(id=id).update(password=hash_password(password))
        return await model.from_queryset_single(User.get(id=id))

    async def change_password(old_password: str, password: str):
        user = await change_user_password()
        return await model.from_orm(user)

    async def get_current_user():
        user = await get_current_active_user()
        return await model.from_orm(user)

    async def set_active_user(id: int, active: bool) -> User:
        await User.filter(id=id).update(is_active=active)
        return await model.from_queryset_single(User.get(id=id))

    async def set_admin_user(id: int, active: bool) -> User:
        await User.filter(id=id).update(is_admin=active)
        return await model.from_queryset_single(User.get(id=id))

    async def set_super_user(id: int, active: bool) -> User:
        await User.filter(id=id).update(is_staff=active)
        return await model.from_queryset_single(User.get(id=id))

    async def set_staff_user(id: int, active: bool) -> User:
        await User.filter(id=id).update(is_superuser=active)
        return await model.from_queryset_single(User.get(id=id))
