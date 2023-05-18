import abc
from datetime import datetime


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, model, id):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, model, filter, value):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, model, updates):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def refresh(self, model):
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def add(self, model):
        self.session.add(model)

    def get(self, model, id):
        return self.session.query(model).filter_by(id=id).first()

    def get_menu(self, model, restaurant_id):
        return self.session.query(model).filter_by(restaurant_id=restaurant_id).first()

    def list(self, model, filter=None, value=None):
        query = self.session.query(model)

        if filter == 'name':
            return query.filter_by(name=value).all()
        elif filter == 'city':
            return query.filter_by(city=value).all()
        elif filter == 'kind':
            return query.filter_by(kind=value).all()

    def update(self, model, updates):
        for key, value in updates.items():
            setattr(model, key, value)
        self.session.add(model)
        return model

    def delete(self, model):
        self.session.delete(model)

    def refresh(self, model):
        self.session.refresh(model)

    def is_owner_existed(self, model, name, phone):
        return self.session.query(model).filter_by(name=name, phone=phone).first()

    def is_restaurant_existed(self, model, owner_id, name, address):
        return self.session.query(model).filter_by(owner_id=owner_id, name=name, address=address).first()

