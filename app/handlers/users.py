from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from app.schema.user import UserCreateSchema, UserLoginSchema
from app.service.user import UserService
from app.service.auth import AuthService
from dependency import get_auth_service, get_user_service
from exception import UserNotFoundException, UserUncorrectedPassword

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/create", response_model=UserLoginSchema)
async def create_user(
    user_data: UserCreateSchema,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        
        result = await user_service.create_user(
            username=user_data.username,
            password=user_data.password
        )

        return result
    
    except Exception as e:
         
        raise HTTPException(
            status_code=400, 
            detail=str(e)
        )
    

@router.post("/auth", response_model=UserLoginSchema)
async def check_user(

    body: UserCreateSchema,
    auth_service: Annotated[AuthService, Depends(get_auth_service)]
):
    
    try:

        return await auth_service.login(body.username, body.password)

           
    except UserNotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )
    
    except UserUncorrectedPassword as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail
        )
    
    