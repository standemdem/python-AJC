from my_package.Classroom import Classroom
from my_package.Eleve import Eleve
# from my_package.Individu import Individu
import random
import os
import sqlite3
random.seed(123)


def start_menu():
    print("Welcome to Class Manager ")
    print("1) Add a student ")
    print("2) Remove a students ")
    print("3) Display all students ")
    print("4) Display general mean ")
    print(" Press any other key to quit Class Manager")
    return input()

if __name__=="__main__":
    classroom = Classroom()
    classroom.init_db()

    while True:
        choice = start_menu() 
        if choice == "1":
            first_name = input("Enter your first name ")
            last_name = input("Enter your last_name ")
            birthdate = input("Enter your age ")
            student_id = random.randint(1, 523)
            general_mean = input("Enter your general mean :")
            student = Eleve(first_name, last_name, birthdate, student_id, general_mean)
            classroom.add_student(student)
            classroom.add_student_to_db(student)
            os.system("cls")
        elif choice == "2":
            classroom.display_students()
            # Supprimer un élève
            classroom.remove_student()

        elif choice == "3":
            os.system("cls")
            classroom.display_students()
        elif choice =="4":
            os.system("cls")
            classroom.get_average_grade()
        else:
            break




    print("success") 