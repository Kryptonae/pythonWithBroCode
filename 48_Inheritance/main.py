class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
class Dog(Animal):
    def speak(self):
        print("BARK!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEAK!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Squeaky")

# print(dog)
print(dog.name)
print(dog.isAlive)
dog.eat()
dog.sleep()
dog.speak()

print()

# print(cat)
print(cat.name)
print(cat.isAlive)
cat.eat()
cat.sleep()
cat.speak()

print()

# print(mouse)
print(mouse.name)
print(mouse.isAlive)
mouse.eat()
mouse.sleep()
mouse.speak()