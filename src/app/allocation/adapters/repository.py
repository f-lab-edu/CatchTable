import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, entity, filter, value):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, entity, filter, value, updates):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, entity, filter, value):
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def add(self, entity):
        self.session.add(entity)

    def get(self, entity, filter, value):
        query = self.session.query(entity)

        if filter == 'id':
            return query.filter_by(id=value).all()
        elif filter == 'name':
            return query.filter_by(name=value).all()
        elif filter == 'city':
            return query.filter_by(city=value).all()
        elif filter == 'kind':
            return query.filter_by(kind=value).all()
        elif filter == 'restaurant_id':
            return query.filter_by(restaurant_id=value).all()

    def update(self, entity, filter, value, updates):
        objects = self.get(entity, filter, value)
        for key, value in updates.items():
            setattr(objects[0], key, value)
        self.session.add(objects[0])
        return objects[0]

    def delete(self, entity, filter, value):
        objects = self.get(entity, filter, value)
        for object in objects:
            self.session.delete(object)

