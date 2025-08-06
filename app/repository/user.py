from app.models.model import UserOrm
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(
            self, 
            username: str, 
            password: str,
            access_token: str
            ) -> UserOrm:
        
        query = (

            insert(UserOrm).values(
                username=username,
                password=password,
                access_token=access_token
            )
        ).returning(UserOrm)

        result = await self.session.execute(query)

        await self.session.commit()

        return result.scalar_one()
    
    async def get_user_by_id(
            self,
            user_id: int
    ) -> UserOrm | None:
        
        query = select(UserOrm).where(UserOrm.id == user_id)

        result = await self.session.execute(query)

        return result.scalar_one_or_none()


        
            
        
    
        


            
        