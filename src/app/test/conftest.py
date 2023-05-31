
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.allocation.entrypoints.dependencies import get_uow
from app.allocation.entrypoints.fastapi_app import app
from app.test.integration import fake_unit_of_work
from app.allocation.domain import model
from app.test.unit.owner.conftest import *
from app.test.unit.restaurant.conftest import *
from app.test.unit.menu.conftest import *


engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def override_get_uow():
    model.Base.metadata.drop_all(bind=engine)
    model.Base.metadata.create_all(bind=engine)
    return fake_unit_of_work.FakeUnitOfWork(session_local)


@pytest.fixture(scope="function", autouse=True)
def client(override_get_uow):
    app.dependency_overrides[get_uow] = lambda: override_get_uow
    return TestClient(app)



