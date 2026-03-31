from fastapi import APIRouter
from app.services.user_service import get_users
from app.services.user_service import create_user
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
async def fetch_users():
    return get_users()

@router.post("/users", response_model=UserResponse)
async def add_user(user_data: UserCreate):
    return create_user(user_data)
