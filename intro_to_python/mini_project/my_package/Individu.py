from abc import ABC, abstractclassmethod

class Individu(ABC):

    @abstractclassmethod
    def display_information(self):
        pass