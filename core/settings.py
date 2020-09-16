
APP_NAME = "FastAPI"

DEBUG = 1

HOST_NAME = '127.0.0.1'

PORT = 8000

ALLOWED_HOSTS = []

''' Databases '''
DATABASE_URI = "postgresql://user:password@localhost:5432/db"

TORTOISE_ORM = {
    "connections": {
        # "default": "sqlite://db.sqlite3",
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "localhost",
                "port": "5432",
                "user": "ckam",
                "password": "123456",
                "database": "fastapi_tortoise_mvc"
            }
        },
    },
    "apps": {
        "models": {
            "models": [
                "core.models.accounts",
                # "core.models.events",
                "core.models.blog",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    }
}


''' Security '''
SECRET_KEY = "8fd86aafe0516b6d538b1b4204a62eea83adac12027eebcd15d669b93f62830e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: 30
