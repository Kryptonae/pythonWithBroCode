# class car:
#     def __init__(self, model, year, color, forSale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.forSale = forSale

# import cars as car
from cars import Car
        
car1 = Car("Mustang", 2020, "Red", True)
car2 = Car("Corvette", 2020, "Blue", False)

print(car1)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.forSale)
car1.driveCar()
car1.stopCar()
car1.describeCar()

print("---------------------------------------------------")

print(car2)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.forSale)
car2.driveCar()
car2.stopCar()
car2.describeCar()