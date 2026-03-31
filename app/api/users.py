from fastapi import APIRouter
from app.services.user_service import get_users
from app.schemas.user import UserResponse

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
async def fetch_users():
    return get_users()
