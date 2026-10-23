class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    
    def width(self):
        return f"Width: {self._width:.1f}cm"
    
    @property
    
    def height(self):
        return f"Height: {self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be a positive value.")
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be a positive value.")

rectangle = Rectangle(3, 4)

print(rectangle.width)  # Output: 3
print(rectangle.height)  # Output: 4