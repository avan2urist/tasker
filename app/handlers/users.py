from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from app.schema.user import UserCreateSchema, UserLoginSchema
from app.service.user import UserService
from dependency import get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserLoginSchema)
async def create_user(
    user_data: UserCreateSchema,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        # Добавим логгирование для отладки
        print("Creating user...")  # Проверим, доходит ли сюда
        result = await user_service.create_user(
            username=user_data.username,
            password=user_data.password
        )
        print("User created:", result)  # Проверим результат
        return result
    except Exception as e:
        print("Error:", str(e))  # Логируем ошибку
        raise HTTPException(status_code=400, detail=str(e))