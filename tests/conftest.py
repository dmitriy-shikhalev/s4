import pytest

from s4.connection import get_session


@pytest.fixture
def session():
    with get_session() as session:
        try:
            yield session
        finally:
            session.rollback()
