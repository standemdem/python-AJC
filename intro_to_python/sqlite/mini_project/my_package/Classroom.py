from my_package.Eleve import Eleve
import sqlite3

class Classroom():

    def __init__(self):
        self.students = []

    def add_student(self, student):    
        self.students.append(student)

    def init_db(self):
        # Connect to the database or create a new one if it doesn't exist
        conn = sqlite3.connect('class.db')

        # Create a cursor object to execute SQL statements
        cursor = conn.cursor()

        # Create the first table called "students"
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                age INTEGER,
                grade FLOAT
            )
        ''')
        conn.commit()

    def add_student_to_db(self, student):
        conn = sqlite3.connect('class.db')
        # Create a cursor object to execute SQL statements
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO  students (first_name, last_name, age, grade) 
            VALUES (?, ?, ?, ?)
            ''', (student.first_name, student.last_name, student.age, student.grade)
            )
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def remove_student(self):
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