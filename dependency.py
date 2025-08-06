from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.user import UserRepository
from app.service.user import UserService
from app.db.database import get_db

async def get_user_repository(session: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(session)

async def get_user_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repo)