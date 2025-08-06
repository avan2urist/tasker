
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base
from sqlalchemy import (
    String, ForeignKey
)

class UserOrm(Base):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    username: Mapped[str] = mapped_column(
        String(60),
        unique=True,
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    access_token: Mapped[str] = mapped_column(
        String(355),
        nullable=False
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





