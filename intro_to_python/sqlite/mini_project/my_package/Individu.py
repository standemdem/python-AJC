from abc import ABC, abstractmethod

class Individu(ABC):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @abstractmethod
    def display_information(self):
        pass