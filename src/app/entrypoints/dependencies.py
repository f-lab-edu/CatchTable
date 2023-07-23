from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from app.service_layer import unit_of_work
from app import config
from app.domain import model, schemas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_uow():
    Engine = create_engine(config.get_postgres_uri(), isolation_level="REPEATABLE READ")
    model.Base.metadata.create_all(bind=Engine)
    return unit_of_work.SqlAlchemyUnitOfWork(sessionmaker(bind=Engine))




# openssl rand -hex 32
SECRET_KEY = "9416c7e82785973d4c1971075f1dcefeb91621c4662eb1be0d1b87f1777399f7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
