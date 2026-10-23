class Student:
    
    class__year = 2024  # Class variable
    numStudents = 0  # Class variable to keep track of the number of students
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.numStudents += 1
        
student1 = Student("Alice", 20)
student2 = Student("Bob", 25)
student3 = Student("Charlie", 22)

print("---------------------------------------------------")

print(student1.name,end=" ")
print(student1.age, end=" ")
# print(student1.class__year)
print(Student.class__year)

print(student2.name,end=" ")
print(student2.age, end=" ")
print(Student.class__year)

print(student3.name, end=" ")
print(student3.age, end=" ")
print(Student.class__year)

print("---------------------------------------------------")

print(f"My graduating class of {Student.class__year} has {Student.numStudents} students.")  
print(student1.name)
print(student2.name)
print(student3.name)