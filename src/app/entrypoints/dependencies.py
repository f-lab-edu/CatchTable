from app.service_layer import unit_of_work
from app import config
from app.domain import model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



def get_uow():
    Engine = create_engine(config.get_postgres_uri(), isolation_level="REPEATABLE READ")
    model.Base.metadata.create_all(bind=Engine)
    return unit_of_work.SqlAlchemyUnitOfWork(sessionmaker(bind=Engine))



# 나중에 Token 관련 function
# https://fastapi.tiangolo.com/tutorial/bigger-applications/