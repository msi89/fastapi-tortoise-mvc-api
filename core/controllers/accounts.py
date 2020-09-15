
from fastapi import APIRouter
from core.services.account import AccountService, model
from core.schemas.accounts import UserSchema
from typing import List
from starlette.status import HTTP_201_CREATED

router = APIRouter()

tags = ['accounts']


@router.get('/users', response_model=List[model])
async def get_users():
    return await AccountService.list()


@router.post('/register', response_model=model, status_code=HTTP_201_CREATED)
async def create_users(model: UserSchema):
    return await AccountService.create(model)
