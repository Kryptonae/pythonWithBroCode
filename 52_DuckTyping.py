class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("Woof!")
    
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
class Car:
    
    alive = False  # Cars are not alive, but we can still define this attribute
    
    def speak(self):
        print("Honk!")
    
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)  # This will raise an AttributeError for Car since it doesn't inherit from Animal