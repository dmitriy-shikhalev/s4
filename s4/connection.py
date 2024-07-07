from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from s4.settings import Settings


def get_engine():
    settings = Settings()
    return create_engine(settings.DB_CONNECTION_STRING)


@contextmanager
def get_session():
    engine = get_engine()

    with Session(engine) as session:
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
        finally:
            session.close()
