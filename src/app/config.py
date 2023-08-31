import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_USERNAME: str = os.getenv("DATABASE_USERNAME")
    DB_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
    DB_HOST: str = os.getenv("DATABASE_HOST", default="localhost")
    DB_PORT: str = os.getenv("DATABASE_PORT", default=5432)
    DB_DATABASE: str = os.getenv("DATABASE_NAME")

    DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

settings = Settings()
def get_postgres_uri():
    if settings.DATABASE_URL is None:
        raise ValueError("DATABASE_URL environment variable not set")
    return settings.DATABASE_URL

