word = "APPLE"

# letter = input("Enter a letter: ").upper()

# if letter in word:
#     print(f"✅ The letter '{letter}' is in the word '{word}'.")
# else:
#     print(f"❌ The letter '{letter}' is not in the word '{word}'.")
    
# if letter not in word:
#     print(f"❌ The letter '{letter}' is not in the word '{word}'.")
# else:
#     print(f"✅ The letter '{letter}' is in the word '{word}'.")

# students = {"Ashwani", "Chirag", "Rohit", "Sakshi"}

# student = input("Enter a student name: ").capitalize()

# if student in students:
#     print(f"✅ {student} is a student.")
# else:
#     print(f"❌ {student} is not a student.")

# grades = {"Ashwani": 90, 
#           "Chirag": 85,
#           "Rohit": 78,
#           "Sakshi": 92}

# grade = input("Enter a student name: ").capitalize()

# if grade in grades:
#     for key, value in grades.items():
#         if key == grade:
#             print(f"{key} has a grade of {value}.")
# else:
#     print(f"❌ {grade} is not a student.")

email = "aa1261885@gmail.com"

if "@" in email and "." in email:
    print(f"Valid email address: {email}")
else:
    print(f"Invalid email address: {email}")