from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from core import settings
from core.models.accounts import User
from core.exceptions import bad_credentials, Http400
from core.middlewares.security import verify_password, hash_password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def authenticate(username: str, password: str) -> User:
    user = await User.get(email=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:

    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise bad_credentials()
    except JWTError:
        raise bad_credentials()
    user = await User.get(email=email)
    if user is None:
        raise bad_credentials("Not authorized")
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user.is_active:
        return current_user
    return Http400("Inactive user")


async def get_admin_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user.is_admin:
        return current_user
    return Http400("You are not administrator")


async def get_super_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user.is_superuser:
        return current_user
    return Http400("You are not super user")


async def change_user_password(
    old_password: str,
    current_password: str,
    user: User = Depends(get_current_active_user)
) -> User:
    if not verify_password(old_password, user.password):
        return Http400("Incorrect password")
    user.password = current_password
    user.save()
    return user
