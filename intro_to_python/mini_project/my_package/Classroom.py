from my_package.Eleve import Eleve

class Classroom():

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self):
        # self.students.remove(student)

        key_to_match = input("Nom de la clé à utiliser pour la suppression : ")
        value_to_match = input("Valeur de la clé à supprimer : ")
        removed = False

        for student in self.students:
            if isinstance(student, Eleve) and hasattr(student, key_to_match):
                if getattr(student, key_to_match) == value_to_match:
                    self.students.remove(student)
                    print(f"Student has been deleted..")
                    removed = True
                    break

        if not removed:
            print("There are no students left to remove.")

    def get_students(self):
        pass

    def get_average_grade(self):
        if not self.students :
            print("no students")
        print(sum(int(student.general_mean) for student in self.students)/len(self.students))
    
    def display_students(self):
        if not self.students:
            print("no students to display")
        else:
            for student in self.students:
                [print(key, value) for key, value in student.__dict__.items()]