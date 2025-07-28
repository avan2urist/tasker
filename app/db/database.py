from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker, 
    AsyncAttrs
)
from sqlalchemy.orm import DeclarativeBase
from app.db.config import settings

DATABASE_URL = settings.DATABASE_URL_asyncpg

async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=False 
)

async_session = async_sessionmaker(async_engine)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True