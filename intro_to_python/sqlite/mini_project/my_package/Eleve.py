from .Individu import Individu

class Eleve(Individu):

    def __init__(self, first_name, last_name, age, student_id, grade):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.grade = grade

    def display_information(self):
        [print(f"{key}: {value}") for key, value in self.__dict__.items()]