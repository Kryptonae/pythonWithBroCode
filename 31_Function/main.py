def happyBirthday(name, age):
    print(f"Happy Birthday dear {name}!")
    print(f"You are now {age} Years old.")
    print("Happy Birthday to you!")
    print()
    
# happyBirthday("Abhinav", 14)
# happyBirthday("Ashwani", 21)
# happyBirthday("Kunal", 25)

def displayInvoice(username, amount, dueDate):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due on {dueDate}.")
    
# displayInvoice("Abhinav", 1000, "30-10-2026")

def sum(num1, num2):
    return num1 + num2

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print(f"{num1} + {num2} = {sum(num1, num2)}")

def fullName(firstName, lastName):
    return f"{firstName.capitalize()} {lastName.capitalize()}"

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

print(f"Your full name is: {fullName(firstName, lastName)}")