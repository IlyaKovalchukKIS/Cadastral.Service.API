from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqladmin import ModelView
from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


class Base(DeclarativeBase):
    __abstract__ = True


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    id: номер пользователя
    email: почта пользователя
    hashed_password: хэш пароля
    created_at: дата создания пользователя
    is_active: активен ли пользователь
    is_superuser: является ли пользователь суперпользователем
    is_verified: подтвержден ли пользователь
    cadasters: список проверенных кадастр запросов
    """

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: str
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    is_active: bool
    is_superuser: bool
    is_verified: bool

    cadasters = relationship("Cadaster", back_populates="user")


class Cadaster(Base):
    __tablename__ = 'cadastral'

    id: Mapped[int] = mapped_column(primary_key=True)
    cadaster_number: Mapped[str]  # кадастровый номер
    longitude: Mapped[str]  # долгота
    width: Mapped[str]  # широта
    date_at: Mapped[datetime] = mapped_column(default=datetime.now)
    result: Mapped[bool]

    owner: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user = relationship("User", back_populates="cadasters")


class CadasterAdmin(ModelView, model=Cadaster):
    column_list = [
        'cadaster_number',
        'longitude',
        'width',
        'date_at',
        'result',
        'owner',
        'user',
    ]


class UserAdmin(ModelView, model=User):
    column_list = [
        'id',
        'email',
        'hashed_password',
        'created_at',
        'is_active',
        'is_superuser',
        'is_verified',
        'cadasters',
    ]
