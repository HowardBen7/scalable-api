from dotenv import load_dotenv
import os

# Load environment variables from the .env file
# This makes values like POSTGRES_HOST available to Python
load_dotenv()

# Config class to hold database settings for the app
class Config:
    # Read database host from the environment
    # Use "localhost" as a fallback if the variable is missing
    database_host: str = os.getenv("POSTGRES_HOST", "localhost")

    # Read database port from the environment
    # Convert it to an integer because ports are numbers
    database_port: int = int(os.getenv("POSTGRES_PORT", 5432))

    # Read database name from the environment
    database_name: str = os.getenv("POSTGRES_DB", "scalable_api")

    # Read database username from the environment
    database_user: str = os.getenv("POSTGRES_USER", "postgres")

    # Read database password from the environment
    database_password: str = os.getenv("POSTGRES_PASSWORD", "postgres")

    # Build the full PostgreSQL connection URL from the values above
    # SQLAlchemy uses this URL to connect to the database
    database_url: str = (
        f"postgresql://{database_user}:{database_password}"
        f"@{database_host}:{database_port}/{database_name}"
    )

# Create one reusable config object for the rest of the app to import
config = Config()