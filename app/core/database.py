from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Import the app config so the database URL can be used here
from app.core.config import config

# Create the SQLAlchemy engine using the database URL from config
# echo=True prints SQL queries in the terminal, which is useful for debugging
engine = create_engine(config.database_url, echo=True)

# Create a session factory
# This will be used to create database sessions when the app needs them
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the shared base class for all database models
# Any model that inherits from Base becomes part of SQLAlchemy's table metadata
Base = declarative_base()

# Database session dependency/helper
# Opens a session, gives it to the route, and closes it afterward
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()