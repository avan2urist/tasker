from app.schema.user import UserLoginSchema
from app.repository.user import UserRepository
import string
import random


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository


    async def create_user(self, username: str, password: str) -> UserLoginSchema:
        access_token = self._generate_access_token()
        user = await self.user_repository.create_user(username, password, access_token)
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)

    @staticmethod
    def _generate_access_token() -> str:
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

