
from passlib.context import CryptContext

bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return bcrypt.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)
