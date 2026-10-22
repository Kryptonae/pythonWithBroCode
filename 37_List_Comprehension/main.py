# doubles = []

# for x in range(1, 11):
#     doubles.append(x * 2)
    
# print(doubles)

# for double in doubles:
#     print(double, end=" ")

doubles = [ x * 2 for x in range(1, 11)]
triples = [ y * 3 for y in range(1, 11)]
squares = [ z * z for z in range(1, 11)]

# print(doubles)
# print(triples)
# print(squares)

fruits = ["apple", "banana", "cherry", "date"]

fruit = [ f.upper() for f in fruits]
fruit = [ f[0] for f in fruits]

# print(fruits)
# print(fruit)

numbers = [1, -2, 3, -4, 5, -6]

positiveNumbers = [ x for x in numbers if x >= 0]
negativeNumbers = [ x for x in numbers if x < 0]
# evenNums = [ x for x in numbers if x & 1 == 0]
evenNums = [ x for x in numbers if x % 2 == 0]
oddNums = [ x for x in numbers if x % 2 != 0]

print(positiveNumbers)
print(negativeNumbers)
print(evenNums)
print(oddNums)