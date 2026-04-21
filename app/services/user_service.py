from app.models.user import User
from fastapi import HTTPException, status
from app.core.security import hash_password

# Get all users from the database
# db is the SQLAlchemy session passed in from the route
def get_users(db):
    return db.query(User).all()

def user_email_exists(db, email):
    # Check if a user with the given email already exists in the database
    return db.query(User).filter(User.email == email).first() is not None


# Create a new user in the database
# user_data is the validated input from the UserCreate schema
def create_user(db, user_data):


# Check if the email is already registered to prevent duplicates
    if user_email_exists(db, user_data.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    
    hashed_password = hash_password(user_data.password)
    
    # Create a new User model instance using the incoming data
    user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_password
    )

    # Add the new user to the current database session
    db.add(user)

    # Save the new row to PostgreSQL
    db.commit()

    # Reload the user from the database so it has updated DB values
    # such as the generated id
    db.refresh(user)

    # Return the stored user object
    return user