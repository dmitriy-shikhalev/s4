from sqlalchemy import select

from s4 import models


def test_session(session):
    file_ = models.File(id=5, filename='abc', size=100)
    session.add(file_)
    stmt = select(models.File).filter(models.File.filename == 'abc')
    results = session.execute(stmt).scalars().all()

    assert len(results) == 1
    assert results[0].filename == 'abc'
    assert results[0].size == 100
