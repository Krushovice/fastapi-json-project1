from datetime import date

from sqlalchemy import BigInteger, Date, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class Serial(Base):
    id: Mapped[int] = mapped_column(
        BigInteger(),
        primary_key=True,
    )
    title: Mapped[str] = mapped_column(
        String(120),
        index=True,
    )
    description: Mapped[str] = mapped_column(
        Text(),
        default="",
        server_default="",
    )
    release_date: Mapped[date | None] = mapped_column(
        Date(),
        nullable=True,
    )
    duration: Mapped[int] = mapped_column(
        Integer(),
        default=1,
        server_default="1",
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Serial(id={self.id}, title={self.title!r})"
