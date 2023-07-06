class Animal:

    def __init__(self, args):
        self.age, self.name, self.breed, self.weight, self.category, self.food= args

    def manger(self):
        print(f"{self.name} likes to eat {self.food}")

dogo = [12, "Pedro", "dog", 45, "domestic", "poop"]
def init_class(animal_description):
    keys_list=["age", "name", "breed", "weight", "category", "food"]
    return dict(zip(keys_list, animal_description)).values()

new1=Animal(init_class(dogo))

print(new1.__dict__.keys())
print(new1.__dict__.values())
new1.manger()
