import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.allocation.domain import schemas
from app.allocation.entrypoints.dependencies import get_uow
from app.allocation.entrypoints.fastapi_app import app
from app.test.integration import fake_unit_of_work
from app.allocation.domain import model



@pytest.fixture(scope="session", autouse=True)
def get_session():
    SQLALCHEMY_DATABASE_URL = "sqlite://"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    model.Base.metadata.create_all(bind=engine)
    yield sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def override_get_uow(get_session):
    return fake_unit_of_work.FakeUnitOfWork(get_session)


@pytest.fixture(scope="function", autouse=True)
def client():
    app.dependency_overrides[get_uow] = override_get_uow
    with TestClient(app) as c:
        yield c


@pytest.fixture
def owner_ex():
    return schemas.Owner(name="Hong Gil-Dong",
                         phone="000-111-1111",
                         email="Gil-Dong@gmail.com")

@pytest.fixture
def restaurant_ex(owner_id):
    return schemas.Restaurant(name="starbucks",
                             owner_id=owner_id,
                             description="World Wide Coffe Shop",
                             phone="000-000-0000",
                             address="Seocho-Gu, Bangbae-Dong, 234",
                             city="seoul",
                             kind="cafe")



