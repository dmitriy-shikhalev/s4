from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Table, ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass
from sqlalchemy.orm import relationship


class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""


storage_chunk_table = Table(
    "storage_chunk_table",
    Base.metadata,
    Column("storage_name", ForeignKey("storage.name", ondelete="CASCADE"), primary_key=True),
    Column("chunk_id", ForeignKey("chunks.id", ondelete="CASCADE"), primary_key=True),
)


class Storage(Base):
    __tablename__ = 'storage'

    name: Mapped[str] = mapped_column(String(10), primary_key=True)

    chunks: Mapped[list[Chunk]] = relationship(
        secondary=storage_chunk_table, back_populates="storages",
    )


class File(Base):
    __tablename__ = 'files'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    filename: Mapped[str] = mapped_column(index=True)
    size: Mapped[int]


class Chunk(Base):
    __tablename__ = 'chunks'

    __table_args__ = (
        UniqueConstraint("file_id", "number"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('files.id', ondelete="CASCADE"))
    number = Column(Integer)
    hash = Column(String(256))
    size = Column(Integer)

    storages: Mapped[list[Storage]] = relationship(
        secondary=storage_chunk_table, back_populates="chunks"
    )
