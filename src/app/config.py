import os


def get_postgres_uri():
    host = "db"
    port = 5432
    user, password, db_name = "myuser", "mypassword", "mydb"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
