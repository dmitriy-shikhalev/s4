from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from s4.settings import Settings


def get_engine():
    if not hasattr(get_engine, 'engine'):
        settings = Settings()
        get_engine.engine = create_engine(settings.DB_CONNECTION_STRING)
    return get_engine.engine


@contextmanager
def get_session():
    engine = get_engine()

    with Session(engine) as session:
        yield session
