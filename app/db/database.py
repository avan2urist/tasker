from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker, 
    AsyncAttrs,
    AsyncSession
)
from sqlalchemy.orm import DeclarativeBase
from app.db.config import settings

DATABASE_URL = settings.DATABASE_URL_asyncpg

async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,  
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True  
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True