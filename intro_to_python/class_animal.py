class Animal:

    def __init__(self, args):
        self.age, self.name, self.breed, self.weight, self.category, self.food= args

    def manger(self):
        print(f"{self.name} likes to eat {self.food}")

class MeatEater(Animal):

    def manger(self):
        self.food="meat"
        print(f"{self.name} likes to eat {self.food}")

class SavageMeatEater(MeatEater):

    def my_method(self):
        """ classe d'animaux sauvages qui vivent aussi dans la forêt"""
        pass

    def speak(self):
        print("I leave in the forest")
        

def init_class(animal_description):
    keys_list=["age", "name", "breed", "weight", "category", "food"]
    return dict(zip(keys_list, animal_description)).values()

dogo = [12, "Pedro", "dog", 45, "domestic", "poop"]
loupio = [14, "Loupio", "wolf", 60, "savage", "little children"]


dog = Animal(init_class(dogo))

print(dog.__dict__.keys())
print(dog.__dict__.values())
dog.manger()

wolf = MeatEater(init_class(loupio))
print(wolf.__dict__.keys())
print(wolf.__dict__.values())
wolf.manger()


savage = SavageMeatEater(init_class(loupio))
print(savage.my_method.__doc__)
savage.speak()
