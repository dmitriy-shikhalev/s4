from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    size = Column(Integer)
    hash = Column(String)


class Chunk(Base):
    __tablename__ = 'chunks'

    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('files.id'))
    no = Column(Integer)
    hash = Column(String, nullable=True)
    size = Column(Integer, nullable=True)
