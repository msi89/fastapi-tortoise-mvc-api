from typing import Optional
from tortoise.contrib.pydantic import PydanticModel


class UserSchema(PydanticModel):
    name: str
    username: str
    email: str
    password: Optional[str]
    avatar: Optional[str]
    is_active: bool = True

    class Config:
        orm_mode = True
