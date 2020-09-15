
APP_NAME = "FastAPI"

DEBUG = 1

HOST_NAME = '127.0.0.1'

PORT = 8000

ALLOWED_HOSTS = []

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

# DATABASE_URI = "postgresql://user:password@localhost:5432/db"
