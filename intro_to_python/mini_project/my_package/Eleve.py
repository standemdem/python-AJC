from .Individu import Individu

class Eleve(Individu):

    def __init__(self, first_name, last_name, birthdate, student_id, general_mean):
        super().__init__(first_name, last_name, birthdate)
        self.student_id = student_id
        self.general_mean = general_mean

    def display_information(self):
        [print(f"{key}: {value}") for key, value in self.__dict__.items()]