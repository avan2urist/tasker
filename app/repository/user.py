from dataclasses import dataclass
from app.schema.user import UserLoginSchema


@dataclass
class UserRepository:

    def create_ser(self, username: str, password: str) -> User:
        pass