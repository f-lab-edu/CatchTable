from app.allocation.service_layer import unit_of_work
from app.allocation import config
from app.allocation.domain import model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
    Engine = create_engine(config.get_postgres_uri(), isolation_level="REPEATABLE READ")
    model.Base.metadata.create_all(bind=Engine)
    return sessionmaker(bind=Engine)

def get_uow():
    return unit_of_work.SqlAlchemyUnitOfWork(get_session())



# 나중에 Token 관련 function
# https://fastapi.tiangolo.com/tutorial/bigger-applications/