from abc import ABC, abstractclassmethod

class LivingBeing(ABC):

    @abstractclassmethod
    def eat(self):
        pass
    
    @abstractclassmethod
    def pray(self):
        pass
    
    @abstractclassmethod
    def love(self):
        pass

class Human(LivingBeing):

    def __init__(self, food, god, fetish ):
        self.food = food
        self.god = god
        self.fetish = fetish 
    
    def eat(self):
        print(f"I eat {self.food}, Miam")

    def pray(self):
        print(f"I pray to the mighty {self.god}")

    def love(self):
        print(f"I do fancy a nice {self.love}")
        
class Reptilian(LivingBeing):

    def __init__(self, food, god, fetish ):
        self.food = food
        self.god = god
        self.fetish = fetish 
    
    def eat(self):
        print(f"Me eat {self.food}, Slurp")

    def pray(self):
        print(f"Me worship mighty {self.god} !")

    def love(self):
        print(f"Me like {self.love} very very much!")

# instanciation
new_human = Human("Baby seals", "Zeus", "bath")
new_reptilian = Reptilian("Human", "Zagrabor", "crispy babies")

new_human.eat()
new_human.pray()
new_reptilian.eat()
new_reptilian.pray()