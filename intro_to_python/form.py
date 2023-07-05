# name = str(input("enter your name"))
# first_name = str(input("Enter your first name"))
# email = str(input("Enter your email"))
# address = str(input("Enter your address"))
# city = str(input("Enter your city"))
dickeys = {'name', 'fn'}

dico={
    'name': str(input("Enter your name: \n")),
    'first_name' : str(input("Enter your first name: \n")),
    'email' : str(input("Enter your email")),
    'address' : str(input("Enter your address")),
    'city' : str(input("Enter your city"))
}

print(f"your name is {dico.name} {dico.first_name}. Your mail is: {dico.email} and you leave at {dico.address} in {dico.city} ")
