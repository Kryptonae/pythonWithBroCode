class Student:
    
    count = 0
    totalGPA = 0.0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.totalGPA += gpa
        
    def getInfo(self):
        return f"Name: {self.name}, GPA: {self.gpa}"
    
    @classmethod
    def getStudentCount(cls):
        return f"Total Students: {cls.count}" 
       
    @classmethod
    def getAverageGPA(cls):
        if cls.count > 0:
            return f"Average GPA: {cls.totalGPA / cls.count:.2f}"
        else:
            return "No students available"

student1 = Student("John", 3.5)
student2 = Student("Jane", 3.8)
student3 = Student("Bob", 3.2)

print(Student.getStudentCount())  # Output: Total Students: 3
print(Student.getAverageGPA())    # Output: Average GPA: 3.50