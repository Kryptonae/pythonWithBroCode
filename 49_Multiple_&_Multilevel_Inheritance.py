class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"The {self.name} is eating.")
    def sleep(self):
        print(f"The {self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"The {self.name} is fleeing!")

class Preadator(Animal):
    def hunt(self):
        print(f"The {self.name} is hunting!")

class Rabbit(Prey):
    pass

class Hawk(Preadator):
    pass

class Fish(Prey, Preadator):
    pass

rabbit = Rabbit("Rabbit")
hawk = Hawk("Hawk")
fish = Fish("Fish")

hawk.hunt()
rabbit.flee()
rabbit.eat()
fish.sleep()