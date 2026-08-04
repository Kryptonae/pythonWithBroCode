# WHILE LOOP

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

""" while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") """
    
""" while age < 0:
    print("Age can be below 0")
    age = int(input("Enter your age: ")) """

# print(f"Hello {name}.")
# print(f"I am {age} years old")

""" food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print(f"Bye"); """

num = int(input("Enter a num between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not Valid!")
    num = int(input("Enter a num between 1 and 10: "))
    
print(f"Num: {num}")