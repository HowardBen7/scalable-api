from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Import the user service functions that handle database logic
from app.services.user_service import get_users, create_user

# Import schemas for request validation and response shaping
from app.schemas.user import UserCreate, UserResponse

# Import the database session dependency
from app.core.database import get_db

# Create a router to hold all user-related endpoints
router = APIRouter()

# GET /users
# Returns a list of users from the database
# response_model ensures each returned item matches UserResponse
@router.get("/users", response_model=list[UserResponse])
async def fetch_users(db: Session = Depends(get_db)):
    return get_users(db)

# POST /users
# Accepts incoming user data validated by UserCreate
# Returns safe user data shaped by UserResponse
@router.post("/users", response_model=UserResponse)
async def add_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_data)
