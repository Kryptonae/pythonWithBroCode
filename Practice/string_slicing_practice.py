"""
STRING INDEXING & SLICING PRACTICE
==================================
Rules:
  [start : end : step]
  - start is INCLUSIVE
  - end is EXCLUSIVE
  - negative index = count from the end (-1 is the last char)
  - step = how many chars to jump; -1 = reverse

Har task ka answer khud likho, phir run karke check karo.
"""

credit_number = "1234-5678-9012-3456"
# indexes:        0123456789..............19

# ------------------------------------------------------------------
# TASK 1: first character
# Expected: "1"
# ------------------------------------------------------------------
print(credit_number[0])


# ------------------------------------------------------------------
# TASK 2: last character (use negative index)
# Expected: "6"
# ------------------------------------------------------------------
print(credit_number[-1])


# ------------------------------------------------------------------
# TASK 3: first 4 characters (the "1234")
# Expected: "1234"
# ------------------------------------------------------------------
print(credit_number[0:4])


# ------------------------------------------------------------------
# TASK 4: the "5678" part (indexes 5 to 8)
# Expected: "5678"
# ------------------------------------------------------------------
print(credit_number[5:9])


# ------------------------------------------------------------------
# TASK 5: everything from index 5 to the end
# Expected: "5678-9012-3456"
# ------------------------------------------------------------------
print(credit_number[5:])


# ------------------------------------------------------------------
# TASK 6: last 4 characters (the "3456")
# Expected: "3456"
# ------------------------------------------------------------------
print(credit_number[-4:])


# ------------------------------------------------------------------
# TASK 7: mask the card -> "XXXX-XXXX-XXXX-3456"
# ------------------------------------------------------------------
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")


# ------------------------------------------------------------------
# TASK 8: every 2nd character
# Expected: "13-6891-46"
# ------------------------------------------------------------------
print(credit_number[::2])


# ------------------------------------------------------------------
# TASK 9: every 3rd character
# Expected: "146-136"
# ------------------------------------------------------------------
print(credit_number[::3])


# ------------------------------------------------------------------
# TASK 10: reverse the whole string
# Expected: "6543-2109-8765-4321"
# ------------------------------------------------------------------
print(credit_number[::-1])


# ------------------------------------------------------------------
# TASK 11 (CHALLENGE): Check if the card number is a palindrome
# A palindrome reads the same forwards and backwards.
# Test with "1234-5678-9012-3456" and "1234321"
# ------------------------------------------------------------------
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome(credit_number))
print(is_palindrome("1234321"))


"""
SOLUTIONS / NOTES
=================
credit_number = "1234-5678-9012-3456"

[0]        -> "1"
[-1]       -> "6"
[0:4]      -> "1234"
[5:9]      -> "5678"
[5:]       -> "5678-9012-3456"
[-4:]      -> "3456"
[::2]      -> "13-6891-46"
[::3]      -> "146-136"
[::-1]     -> "6543-2109-8765-4321"

Remember: `end` index ko include NAHI karte.
    "abcdef"[1:4]  ->  "bcd"   (index 1,2,3)
"""
