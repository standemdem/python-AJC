employee_keys = ["Last-name", "First-name", "Age", "Salary", "Position"]
empl1= ["de Montmarin", "Stanislas", 36, 38000, "dev IVVQ"]
empl2= ["Galand", "Juliett", 31, 12000, "balayeuse"]

def lists_to_dict(list_of_keys, list_of_values):
    return dict(zip(list_of_keys, list_of_values))

list_of_employees =[lists_to_dict(employee_keys, value) for value in [empl1, empl2]]

print(list_of_employees)

