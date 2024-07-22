from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass


class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""


class File(Base):
    __tablename__ = 'files'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    filename: Mapped[str]
    size: Mapped[int]
    hash: Mapped[str]


class Chunk(Base):
    __tablename__ = 'chunks'

    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('files.id'))
    no = Column(Integer)
    hash = Column(String, nullable=True)
    size = Column(Integer, nullable=True)
