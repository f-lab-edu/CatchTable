from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.entrypoints.dependencies import get_uow
from app.entrypoints.fastapi_app import app
from tests.unit import fake_unit_of_work
from app.domain import model
import pytest

engine = create_engine("sqlite:///./tests.db", connect_args={"check_same_thread": False})
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



