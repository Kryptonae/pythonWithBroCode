import math
class Shape:
    def __init__(self, color, isFilled):
        self.color = color
        self.isFilled = isFilled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.isFilled else 'not filled'}.")

class Circle(Shape):
    def __init__(self, color, isFilled, radius):
        super().__init__(color, isFilled)
        self.radius = radius
    def describe(self):
        print(f"AREA: {(math.pi * self.radius ** 2):.2f}")
        super().describe()

class Square(Shape):
    def __init__(self, color, isFilled, side):
        super().__init__(color, isFilled)
        self.side = side
    def describe(self):
        print(f"AREA: {(self.side ** 2):.2f}")
        super().describe()
        
class Triangle(Shape):
    def __init__(self, color, isFilled, base, height):
        super().__init__(color, isFilled)
        self.base = base
        self.height = height
    def describe(self):
        print(f"AREA: {(0.5 * self.base * self.height):.2f}")
        super().describe()
        
circle = Circle(color="Red", isFilled=True, radius=5)
square = Square(color="Blue", isFilled=False, side=4)
trianle = Triangle(color="Green", isFilled=True, base=3, height=6)

print(f"Circle: color={circle.color}, isFilled={circle.isFilled}, radius={circle.radius}")
circle.describe()
print()

print(f"Square: color={square.color}, isFilled={square.isFilled}, side={square.side}")
square.describe()
print()

print(f"Triangle: color={trianle.color}, isFilled={trianle.isFilled}, Base={trianle.base}, Height={trianle.height}")
trianle.describe()