from Individu import Individu

class Eleve(Individu):

    def __init__(self, first_name, last_name, birthdate, student_id, gen_mean):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.student_id = student_id
        self.gen_mean = gen_mean

    def display_information(self):
        print(self.__dict__)


eleve1 = Eleve("bob", "bob", 12, "1", 12)
print(eleve1.last_name)