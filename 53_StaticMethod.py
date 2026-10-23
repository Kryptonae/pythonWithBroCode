class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def getInfo(self):
        return f"Name: {self.name}, Position: {self.position}"
    
    @staticmethod
    def isValidPosition(position):
        valid_positions = ["Manager", "Developer", "Designer"]
        return position in valid_positions
        
employee1 = Employee("Alice", "Manager")
print(employee1.getInfo())  # Output: Name: Alice, Position: Manager

print(Employee.isValidPosition("Developer"))  # Output: True
print(Employee.isValidPosition("Engineer"))  # Output: False