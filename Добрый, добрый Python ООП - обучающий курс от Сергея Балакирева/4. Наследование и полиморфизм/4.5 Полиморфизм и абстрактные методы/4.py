
from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return f"Базовый класс Model"


class ModelForm(Model):
    counter = 0

    def __init__(self, login, password):
        self._id = self.__generate_id()
        self._login = login
        self._password = password

    def get_pk(self):
        return self._id

    @classmethod
    def __generate_id(cls):
        cls.counter += 1
        return cls.counter