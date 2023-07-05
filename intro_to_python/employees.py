# Library needed to clear the screen on the terminal
import os

employee_keys = ["Last-name", "First-name", "Age", "Salary", "Position"]

def create_employee():
    # asks for user inputs
    # returns a list of those inputs
    first_name = input("entre un nom: \n")  
    last_name=input("entre un prénom: \n")
    age=input("entre un age: \n")
    salary=input("entre un salaire: \n")
    position=input("entre un role: \n")
    return [first_name, last_name, age, salary, position]

def lists_to_dict(list_of_keys, list_of_values):
    # zip(list1, list2) joins two lists together by their indexes
    # dict turns the zip object created into a dictionnary
    return dict(zip(list_of_keys, list_of_values))
    
def start_menu():
    print("1) Add an employee")
    print("2) Display all employees")
    print("3) Exit the program")
    return input()

# initialize an empty list to store all employees created in the future    
list_of_all_employees=[]

while True:
    user_input = start_menu()

    if user_input == "1":  
        #clears the console on linux (for windows, use "cls")     
        os.system("clear") 
        # ask for user input and creates a new dict
        new_employee = lists_to_dict(employee_keys, create_employee()) 
        # appends the dict to a list of employees
        list_of_all_employees.append(new_employee)

    elif user_input == "2":
        os.system("clear")
        print(list_of_all_employees)
        
    else:
        break