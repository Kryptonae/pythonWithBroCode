# String Method
""" 
# name = input("Enter your name: ")
phoneNumber = input("Enter your Phone Number: ")

# result = len(name)
# result = name.find("A")
# result = name.rfind("i")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()

# result = phoneNumber.count("-")
result = phoneNumber.replace("-", "")


print(result)
"""

# Exercise 

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters long")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain digits")
else:
    print(f"Hello {username}")