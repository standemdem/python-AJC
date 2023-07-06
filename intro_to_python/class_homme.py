class Human:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age

    def get_older(self):
        self.age +=1
        print(f"you are now: {self.age}")

    def display_human(self):
        print(f"My name is {self.first_name} and I am {self.age} years old")

human1 = Human("stan", 3)
print(human1.first_name)

human1.display_human()