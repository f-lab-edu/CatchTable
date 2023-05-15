from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    JSON,
)
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import registry as mapper
from app.allocation.domain import model

metadata = MetaData()

Owner = Table(
    "owner",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("phone", String(255)),
    Column("email", String(255)),
    Column("date_of_creation", DateTime, default=datetime.now),
    Column("date_of_update", DateTime, default=datetime.now)
)

Restaurant = Table(
    "restaurant",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("owner_id", ForeignKey('owner.id')),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("phone", String(255)),
    Column("address", String(255)),
    Column("city", String(255)),
    Column("kind", String(255)),
    Column("date_of_creation", DateTime, default=datetime.now),
    Column("date_of_update", DateTime, default=datetime.now),
)

Menu = Table(
    "menu",
    metadata,
    Column("restaurant_id", ForeignKey('restaurant.id'), primary_key=True),
    Column("menu", JSON),
    Column("date_of_creation", DateTime, default=datetime.now),
    Column("date_of_update", DateTime, default=datetime.now)
)

def start_mappers():
    mapper().map_imperatively(model.Owner, Owner)
    mapper().map_imperatively(model.Restaurant, Restaurant,
                              properties={"owner": relationship(model.Owner)})
    mapper().map_imperatively(model.Menu, Menu,
                              properties={"restaurant": relationship(model.Restaurant)})


# orm.start_mappers()
# orm.metadata.create_all(bind=unit_of_work.Engine)