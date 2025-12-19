from fastapi import APIRouter, Depends, status
from .schemas import UserCreateModel, UserModel
from .service import UserService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException

auth_router = APIRouter()
user_service = UserService()

@auth_router.post(
        "/signup", 
        response_model=UserModel,
        status_code=status.HTTP_201_CREATED
        )
async def create_user_acc(
    user_data: UserCreateModel,
    session: AsyncSession = Depends(get_session)  #remember get_session is the dependency we created at(check the path) ie why depends is used here
    ):
    email = user_data.email
    user_exists = await user_service.user_exists(email, session)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with email already exists")
    new_user = await user_service.create_user(user_data, session)
    return new_user

