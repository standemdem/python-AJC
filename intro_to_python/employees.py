# empl1= ["de Montmarin", "Stanislas", 36, 38000, "dev IVVQ"]
# empl2= ["Galand", "Juliett", 31, 12000, "balayeuse"]
# list_of_all_employees=[empl1, empl2]


# all_employees =[lists_to_dict(employee_keys, value) for value in list_of_all_employees]
# def create_employee():
#     first_name = input("Enter a first name: ")
#     last_name = input("Enter a last name: ")
#     # Rest of the code...


# create_employee()
employee_keys = ["Last-name", "First-name", "Age", "Salary", "Position"]
def lists_to_dict(list_of_keys, list_of_values):
    return dict(zip(list_of_keys, list_of_values))

def create_employee():
    res=[]
    first_name = input("entre un nom: \n")  
    last_name=input("entre un prénom: \n")
    age=input("entre un age: \n")
    salary=input("entre un salaire: \n")
    position=input("entre un role: \n")
    res= [first_name, last_name, age, salary, position]
    print(type(res))
    return res

def start_menu():
    print("1) Add an employee")
    print("2) Display all employees")
    print("3) Exit the program")
    res= input()
    return res
    
list_of_all_employees=[]
while True:
    user_input = start_menu()
    test=[]
    if user_input == "1":
        test=create_employee()
        new_employee = lists_to_dict(employee_keys, test)
        list_of_all_employees.append(new_employee)
        
    elif user_input == "2":
        print(list_of_all_employees)
        
    else:
        break

# create_employee()