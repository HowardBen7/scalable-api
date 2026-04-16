from fastapi import FastAPI

# Import the users router so user related endpoints can be added to the app
from app.api.users import router as users_router

# Import the SQLAlchemy Base and engine so tables can be created
from app.core.database import Base, engine

# Import the User model so SQLAlchemy knows this table exists
# This matters because create_all only creates tables for models that have been loaded
from app.models.user import User

# Create database tables from all loaded models
Base.metadata.create_all(bind=engine)

# Create the main FastAPI application instance
app = FastAPI()

# Register the users router so routes like /users become part of the app
app.include_router(users_router)

# Simple root route to confirm the API is running
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}