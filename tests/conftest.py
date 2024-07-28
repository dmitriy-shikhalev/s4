import pytest

from s4.connection import get_session


@pytest.fixture
def session():
    with get_session() as session_:
        try:
            yield session_
        finally:
            session_.rollback()
