from fastapi import APIRouter
from core.controllers import accounts

router = APIRouter()

router.include_router(accounts.router, prefix='/accounts', tags=accounts.tags)
