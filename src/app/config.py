import os


def get_postgres_uri():
    SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URL is None:
        raise ValueError("DATABASE_URL environment variable not set")

    return SQLALCHEMY_DATABASE_URL
