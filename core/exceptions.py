from fastapi import HTTPException, status
from typing import Optional


def bad_credentials(msg="Could not validate credentials"):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=msg,
        headers={"WWW-Authenticate": "Bearer"},
    )


def raise_authenticate(msg="Incorrect username or password"):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=msg,
        headers={"WWW-Authenticate": "Bearer"},
    )


def raise_exception(msg: Optional[str], status: Optional[int], headers: Optional[any]):
    raise HTTPException(
        status_code=status,
        detail=msg,
        headers=headers,
    )


def Http400(message=Optional[str]):
    raise HTTPException(status_code=400, detail=message)


def Http404(message=Optional[str]):
    raise HTTPException(status_code=404, detail=message)
