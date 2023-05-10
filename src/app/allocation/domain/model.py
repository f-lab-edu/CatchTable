from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    JSON,
)
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Owner(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    phone = Column(String(255))
    email = Column(String(255))
    date_of_creation = Column(DateTime, default=datetime.now)
    date_of_update = Column(DateTime, default=datetime.now)

    restaurants = relationship("Restaurant", back_populates="owner")

class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(ForeignKey('owner.id'))
    name = Column(String(255))
    description = Column(String(255))
    phone = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    kind = Column(String(255))
    date_of_creation = Column(DateTime, default=datetime.now)
    date_of_update = Column(DateTime, default=datetime.now)

    owner = relationship("Owner", back_populates="restaurants")


class Menu(Base):
    __tablename__ = "menu"
    id = Column(ForeignKey('restaurant.id'), primary_key=True)
    menu = Column(JSON)
    date_of_creation = Column(DateTime, default=datetime.now)
    date_of_update = Column(DateTime, default=datetime.now)

