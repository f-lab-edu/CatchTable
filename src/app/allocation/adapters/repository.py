import abc
from typing import Set, List
from app.allocation.domain import model, schema

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, entity, filter, value):
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def add(self, entity):
        self.session.add(entity)

    def get(self, entity, filter, value):
        query = self.session.query(entity)

        if filter == 'name':
            return query.filter_by(name=value).all()
        elif filter == 'city':
            return query.filter_by(city=value).all()
        elif filter == 'kind':
            return query.filter_by(kind=value).all()

