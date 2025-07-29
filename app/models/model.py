from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base
from sqlalchemy import (
    String, DateTime, Boolean, ForeignKey
)

class UserOrm(Base):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )

    id_tg: Mapped[str] = mapped_column(
        String(250),
        unique=True,
        nullable=False
    )

    invite_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=None),
        default=lambda: datetime.now()
    )

    is_leaved: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

class ProductOrm(Base):

    __tablename__ = "Product"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )
    


