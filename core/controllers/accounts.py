
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError
from core.services.account import AccountService, model
from core.schemas.accounts import UserSchema, UserUpdateSchema
from typing import List
from starlette.status import HTTP_201_CREATED
from fastapi import Depends
from core.middlewares.auth import get_current_active_user

router = APIRouter()

tags = ['accounts']


@router.get('/users', response_model=List[model])
async def get_users_list(token: str = Depends(get_current_active_user)):
    return await AccountService.get()


@router.get('/{user_id}', response_model=model)
async def get_user_by_id(user_id: int):
    return await AccountService.get(id=user_id)


@router.put('/{user_id}', response_model=model)
async def update_user_data(user_id: int, user: UserUpdateSchema):
    return await AccountService.update(user_id, user)


@router.put('/{user_id}/reset_password', response_model=model)
async def reset_user_password(user_id: int, password: str):
    return await AccountService.reset_user_password(user_id, password)


@router.patch('/change_password', response_model=model)
async def change_user_password(old_password: str, password: str, token: str = Depends(get_current_active_user)):
    return await AccountService.change_password(old_password, password)


@router.patch('/current')
async def current_user(token: str = Depends(get_current_active_user)):
    print('===TOKEN:', token)
    return await AccountService.get_current_user()


@router.post('/signup', response_model=model, status_code=HTTP_201_CREATED)
async def sign_up(model: UserSchema):
    return await AccountService.create(model)


@router.post('/signin')
async def sign_in(email: str, password: str):
    return await AccountService.sign_in(email, password)
