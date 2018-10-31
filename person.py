from query import Query

class Person:

    _all = []

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person._all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    @classmethod
    def all(cls):
        return cls._all
