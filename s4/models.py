from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Table, List, relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass


class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""


storage_chunk_table = Table(
    "association_table",
    Base.metadata,
    Column("storage_name", ForeignKey("storage.name"), primary_key=True),
    Column("chunk_storage", ForeignKey("chunk.storage"), primary_key=True),
)


class Storage(Base):
    __tablename__ = 'storage'

    name: Mapped[str] = mapped_column(String(10), primary_key=True)

    chunks: Mapped[List[Chunk]] = relationship(
        secondary=storage_chunk_table, back_populates="storages"
    )


class File(Base):
    __tablename__ = 'files'

    filename: Mapped[str] = mapped_column(primary_key=True)
    size: Mapped[int]


class Chunk(Base):
    __tablename__ = 'chunks'

    file_id = Column(Integer, ForeignKey('files.id'), primary_key=True)
    number = Column(Integer, primary_key=True)
    hash = Column(String)
    size = Column(Integer)

    storages: Mapped[List[Chunk]] = relationship(
        secondary=storage_chunk_table, back_populates="chunks"
    )
