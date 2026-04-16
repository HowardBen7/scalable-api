from app.models.user import User

# Get all users from the database
# db is the SQLAlchemy session passed in from the route
def get_users(db):
    return db.query(User).all()

# Create a new user in the database
# user_data is the validated input from the UserCreate schema
def create_user(db, user_data):
    # Create a new User model instance using the incoming data
    user = User(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password
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