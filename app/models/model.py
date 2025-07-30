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
        nullable=False
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

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )


class SalledProductOrm(Base):

    __tablename__ = "salled_product"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE")
    )





