from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    database_host: str = os.getenv("POSTGRES_HOST", "localhost")
    database_port: int = int(os.getenv("POSTGRES_PORT", 5432))
    database_name: str = os.getenv("POSTGRES_DB", "scalable_api")
    database_user: str = os.getenv("POSTGRES_USER", "postgres")
    database_password: str = os.getenv("POSTGRES_PASSWORD", "postgres")

    database_url: str = (f"postgresql://{database_user}:{database_password}"
                         f"@{database_host}:{database_port}/{database_name}")

config = Config()