import uvicorn
from core.settings import HOST_NAME, PORT, DEBUG


if __name__ == "__main__":
    uvicorn.run('core:app', host=HOST_NAME, port=PORT, debug=DEBUG)
