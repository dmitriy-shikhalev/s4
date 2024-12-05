import uvicorn

from s4.router import app
from s4.settings import Settings


def router():
    settings = Settings()
    uvicorn.run(app, host=settings.host, port=settings.port)
