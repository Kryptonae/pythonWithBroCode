"""
STRING METHODS PRACTICE
=======================
Har exercise ke neeche `# TODO` likha hai — apna answer likho,
phir file run karke check karo. Solutions neeche comment me hain.
"""

# ------------------------------------------------------------------
# TASK 1: len()
# text = "Hello World"
# Expected output: 11
# ------------------------------------------------------------------
text = "Hello World"
print(len(text))


# ------------------------------------------------------------------
# TASK 2: find()  -> returns index, -1 if not found
# text = "programming"
# Find the index of "g". Expected: 3  (first g is at index 3)
# ------------------------------------------------------------------
text = "programming"
print(text.find("g"))


# ------------------------------------------------------------------
# TASK 3: rfind() -> finds from the RIGHT (last occurrence)
# text = "programming"
# Find the LAST index of "g". Expected: 10
# ------------------------------------------------------------------
text = "programming"
print(text.rfind("g"))


# ------------------------------------------------------------------
# TASK 4: capitalize() -> first letter upper, rest lower
# text = "hELLO wORLD"
# Expected: "Hello world"
# ------------------------------------------------------------------
text = "hELLO wORLD"
print(text.capitalize())


# ------------------------------------------------------------------
# TASK 5: upper() and lower()
# text = "PyThOn"
# Print it in full UPPER then full lower.
# Expected: "PYTHON" then "python"
# ------------------------------------------------------------------
text = "PyThOn"
print(text.upper())
print(text.lower())


# ------------------------------------------------------------------
# TASK 6: isdigit() -> True if all chars are numbers
# Check these and print the result:
#   "12345"  -> True
#   "12a45"  -> False
# ------------------------------------------------------------------
print("12345".isdigit())
print("12a45".isdigit())


# ------------------------------------------------------------------
# TASK 7: isalpha() -> True if all chars are letters
# Check these:
#   "Python" -> True
#   "Python3" -> False
#   "Hello World" -> False (space is not a letter)
# ------------------------------------------------------------------
print("Python".isalpha())
print("Python3".isalpha())
print("Hello World".isalpha())


# ------------------------------------------------------------------
# TASK 8: count() -> counts how many times a char/substring appears
# text = "banana"
# Count "a". Expected: 3
# ------------------------------------------------------------------
text = "banana"
print(text.count("a"))


# ------------------------------------------------------------------
# TASK 9: replace() -> replaces all occurrences
# phone = "123-456-7890"
# Remove all dashes. Expected: "1234567890"
# ------------------------------------------------------------------
phone = "123-456-7890"
print(phone.replace("-", ""))


# ------------------------------------------------------------------
# TASK 10 (CHALLENGE): Combine everything
# Write a function that takes a username and validates:
#   - length must be <= 12
#   - no spaces
#   - only letters (isalpha)
# Print a friendly message for each case.
# ------------------------------------------------------------------
def validate_username(username):
    if len(username) > 12:
        return "Too long (max 12 characters)"
    elif " " in username:
        return "No spaces allowed"
    elif not username.isalpha():
        return "Letters only"
    else:
        return f"Hello {username}"

print(validate_username("Ashwani"))
print(validate_username("Ashwani123"))
print(validate_username("Ash wani"))
print(validate_username("ThisNameIsWayTooLong"))


"""
SOLUTIONS / NOTES
=================
len("Hello World")          -> 11
"programming".find("g")     -> 3
"programming".rfind("g")    -> 10
"hELLO wORLD".capitalize()  -> "Hello world"
"PyThOn".upper()            -> "PYTHON"
"PyThOn".lower()            -> "python"
"12345".isdigit()           -> True
"12a45".isdigit()           -> False
"Python".isalpha()          -> True
"Python3".isalpha()         -> False
"banana".count("a")         -> 3
"123-456-7890".replace("-", "") -> "1234567890"
"""
