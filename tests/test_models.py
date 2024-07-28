import pytest

from s4 import models


def test_session(session):
    file_ = models.File(id=5, filename='abc', size=100)
    session.add(file_)
    raise ZeroDivisionError(session)
