import abc
from app.domain import model as domain


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, model, id):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, model):
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

    def get_user(self, model, email):
        return self.session.query(model).filter_by(email=email).first()

    def get_menu(self, restaurant_id):
        return (
            self.session.query(domain.Menu)
            .filter_by(restaurant_id=restaurant_id)
            .first()
        )

    def list(self, model):
        return self.session.query(model).all()

    def list_restaurants(self, model, filter=None, value=None):
        query = self.session.query(model)

        if filter == "name":
            return query.filter_by(name=value).all()
        elif filter == "city":
            return query.filter_by(city=value).all()
        elif filter == "kind":
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

    def is_user_existed(self, model, email):
        return self.session.query(model).filter_by(email=email).first()

    def is_restaurant_existed(self, owner_id, name, address):
        return (
            self.session.query(domain.Restaurant)
            .filter_by(owner_id=owner_id, name=name, address=address)
            .first()
        )
