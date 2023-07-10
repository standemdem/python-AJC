from my_package.Eleve import Eleve
import sqlite3, os

class Classroom():

    def __init__(self):
        self.students = []
        # Connect to the database or create a new one if it doesn't exist
        self.conn = sqlite3.connect('class.db')
        # Create a cursor object to execute SQL statements
        self.cursor = self.conn.cursor()

    def add_student(self, student):    
        self.students.append(student)

    def read_query(self, filename):
        with open(filename, "r") as f:
            query = f.read()
        return query

    def execute_querry(self, query):
        self.cursor.executescript(query)

    def close_connexion(self):
        self.conn.close()

    def init_db(self):
        # Create the tables
        create_table_path = r"C:\Users\utilisateur\Documents\projects\intro_to_python\sqlite\mini_project\my_package\sql_queries\create_table.sql"
        create_table = self.read_query(create_table_path)
        self.execute_querry(create_table)
        self.conn.commit()
        return create_table
        

    def add_student_to_db(self, student):
        query_path = r"C:\Users\utilisateur\Documents\projects\intro_to_python\sqlite\mini_project\my_package\sql_queries\insert_student.sql"
        cursor = self.conn.cursor()
        new_student = self.read_query(query_path)
        cursor.execute(new_student, (student.first_name, student.last_name, student.age, student.grade))
        self.conn.commit()

    def remove_student(self, input_id):
        query_path = r"C:\Users\utilisateur\Documents\projects\intro_to_python\sqlite\mini_project\my_package\sql_queries\delete_student.sql"
        cursor = self.conn.cursor()
        delete_query = self.read_query(query_path)
        cursor.execute(delete_query, input_id)
        self.conn.commit()

    def get_average_grade(self):
        if not self.students :
            print("no students")
        print(sum(int(student.general_mean) for student in self.students)/len(self.students))
    
    def display_students(self):
        query_path = r"C:\Users\utilisateur\Documents\projects\intro_to_python\sqlite\mini_project\my_package\sql_queries\select_table.sql"
        cursor = self.conn.cursor()
        students = self.read_query(query_path)
        cursor.execute(students)
        students = cursor.fetchall()

        if not students:
            print("no students to display")
        else:
            for student in students:
                a, b, c, d, e =student
                print(f"id: {a} name: {c} {b} age: {d} grade: {e}")
                print("----------------------\n")