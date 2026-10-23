class Car:
    def __init__(self, model, year, color, forSale):
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale
    def driveCar(self):
        print(f"You are driving the car {self.model}")
    def stopCar(self):
        print(f"The car {self.model} has stopped")
    def describeCar(self):
        print(f"The car {self.model} is a {self.color} color and was made in {self.year}. It is {'for sale' if self.forSale else 'not for sale'}.")