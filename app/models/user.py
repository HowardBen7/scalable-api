from sqlalchemy import Column, Integer, String
from app.core.database import Base

# SQLAlchemy model for the users table
# Each class attribute becomes a column in PostgreSQL
class User(Base):
    # Name of the table in the database
    __tablename__ = "users"

    # Primary key for uniquely identifying each user row
    id = Column(Integer, primary_key=True, index=True)

    # User's name, stored as text
    # Indexed to make lookups/filtering faster
    name = Column(String, index=True)

    # User's email, stored as text
    # unique=True prevents duplicate emails
    # index=True helps make lookups faster
    email = Column(String, unique=True, index=True)

    # User's password, stored as text
    # This should be hashed 
    password = Column(String)