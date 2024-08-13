from datetime import datetime

from sqladmin import ModelView
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True


class Cadaster(Base):
    __tablename__ = 'cadastral'

    id: Mapped[int] = mapped_column(primary_key=True)
    cadaster_number: Mapped[str]  # кадастровый номер
    longitude: Mapped[str]  # долгота
    width: Mapped[str]  # широта
    date_at: Mapped[datetime] = mapped_column(default=datetime.now)
    result: Mapped[bool]


class CadasterAdmin(ModelView, model=Cadaster):
    column_list = [
        'cadaster_number',
        'longitude',
        'width',
        'date_at',
        'result',
    ]
