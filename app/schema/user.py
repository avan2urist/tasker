from pydantic import BaseModel, Field

class UserLoginSchema(BaseModel):
    user_id: int 
    access_token: str

class UserCreateSchema(BaseModel):
    username: str = Field(min_length = 6)
    password: str = Field(min_length = 6)