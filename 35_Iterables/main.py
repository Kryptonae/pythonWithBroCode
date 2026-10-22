# numbers = [1, 2, 3, 4, 5]
numbers = (1, 2, 3, 4, 5)


for number in numbers:
    print(number, end=" ")
    
print()
    
for number in reversed(numbers):
    print(number, end=" ")
    
print()

fruits = ["apple", "banana", "cherry", "date"]
# fruits = {"apple", "banana", "cherry", "date"}

for fruit in fruits:
    print(fruit, end=" ")
    
print()

name = "Ashwani Kumar"

for character in name:
    print(character, end=" ")
    
print()

myDictorinary = {"name": "Ashwani", "age": 30, "city": "New York"}

for key, value in myDictorinary.items():
    print(key, ":", value)