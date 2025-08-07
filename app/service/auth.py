from app.repository.user import UserRepository
from app.schema.user import UserLoginSchema
from exception import UserNotFoundException, UserUncorrectedPassword


class AuthService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def login(self, username: str, password: str) -> UserLoginSchema:

        user = await self.user_repository.get_user_by_username(username)

        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserUncorrectedPassword
        
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)