from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import logging
from core import settings
from core.routes import router


app = FastAPI()
register_tortoise(app, config=settings.TORTOISE_ORM, generate_schemas=True,
                  add_exception_handlers=True)
app.include_router(router)


@app.on_event('startup')
async def onstartup():
    logging.info('app is started...')


@app.on_event('shutdown')
async def onshutdown():
    logging.info('app is stopped...')
