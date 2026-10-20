"""
============================================================
  FILE: string_master_practice.py
  THEME: SECRET AGENT TERMINAL  🕵
  Combines: String Methods + Indexing/Slicing
============================================================

  Rules recap:
    METHOD                          | KAAM
    --------------------------------|---------------------------
    len(x)                          | length
    x.find(sub) / x.rfind(sub)      | pehla / aakhri index (-1 = nahi mila)
    x.capitalize()                  | First upper, baaki lower
    x.upper() / x.lower()           | sab upper / lower
    x.title()                       | Har Word Ka First Upper
    x.isdigit() / x.isalpha()       | sab numbers? / sab letters?
    x.count(sub)                    | kitni baar aaya
    x.replace(a, b)                 | a ko b se badlo
    x.strip()                       | aage-peeche ke spaces hatao
    x.split(sep)                    | string ko list me todo

    SLICE  [start : end : step]
      start INCLUSIVE, end EXCLUSIVE
      [::2]  -> har 2nd char      [::-1] -> reverse
      [-4:]  -> last 4 chars       [:4]   -> first 4 chars
============================================================
"""

# ==========================================================
# MISSION 1: CREDIT CARD MASKING
# Card number: "1234-5678-9012-3456"
# Sirf last 4 digits dikhao, baaki X. Output:
#   "XXXX-XXXX-XXXX-3456"
# Uses: slicing [-4:]
# ==========================================================
card = "1234-5678-9012-3456"
masked = f"XXXX-XXXX-XXXX-{card[-4:]}"
print("1) Masked card :", masked)


# ==========================================================
# MISSION 2: USERNAME VALIDATOR
# Rules:
#   - max 12 characters
#   - no spaces
#   - only letters (no digits)
# Uses: len(), in, isalpha()
# ==========================================================
def validate_username(name):
    if len(name) > 12:
        return "REJECTED: > 12 characters"
    elif " " in name:
        return "REJECTED: spaces not allowed"
    elif not name.isalpha():
        return "REJECTED: letters only"
    else:
        return f"ACCEPTED: Welcome, Agent {name}!"

print("2) 'AgentX'    :", validate_username("AgentX"))
print("2) 'Agent 007' :", validate_username("Agent 007"))
print("2) 'SuperLongAgentName' :", validate_username("SuperLongAgentName"))


# ==========================================================
# MISSION 3: DECODE THE SECRET MESSAGE
# Intercepted signal (every 2nd char is real, rest is noise):
#   "hXeXlXlXoX"
# Real message = string[::2]. Decode it!
# Uses: slicing [::2]
# ==========================================================
signal = "hXeXlXlXoX"
secret = signal[::2]
print("3) Decoded     :", secret)


# ==========================================================
# MISSION 4: REVERSE THE CODE
# Enemy's code: "retupmoC"
# Reverse it to get the real word. Uses: [::-1]
# ==========================================================
enemy_code = "retupmoC"
real_word = enemy_code[::-1]
print("4) Reversed    :", real_word)


# ==========================================================
# MISSION 5: PALINDROME CHECK
# A palindrome same reads forwards & backwards.
# Check these codes: "1234321" and "1234-5678-9012-3456"
# Uses: [::-1]
# ==========================================================
def is_palindrome(s):
    return s == s[::-1]

print("5) '1234321'   :", "Palindrome" if is_palindrome("1234321") else "Not Palindrome")
print("5) card        :", "Palindrome" if is_palindrome(card) else "Not Palindrome")


# ==========================================================
# MISSION 6: NAME FORMATTER
# Messy input: "  aShWaNi   kUmAr  "
# 1. strip spaces, 2. split into words, 3. capitalize each
# Output: "Ashwani Kumar"
# Uses: strip(), split(), capitalize()
# ==========================================================
messy = "  aShWaNi   kUmAr  "
words = messy.strip().split()
clean_name = " ".join(w.capitalize() for w in words)
print("6) Clean name  :", clean_name)


# ==========================================================
# MISSION 7: COUNT THE DANGER SIGNALS
# Message: "red red blue red green"
# Count how many times "red" appears. Uses: count()
# ==========================================================
message = "red red blue red green"
print("7) 'red' count :", message.count("red"))


# ==========================================================
# MISSION 8: SPY ID PARSER  (final boss 🐉)
# ID format: "AGENT-007-XYZ"
#   start = "AGENT"
#   number = middle part
#   code = last 3 letters (use negative slicing)
# Uses: slicing + startswith + split
# ==========================================================
spy_id = "AGENT-007-XYZ"
parts = spy_id.split("-")
role = parts[0]
number = parts[1]
code = spy_id[-3:]

print("8) Role        :", role)
print("8) Number      :", number)
print("8) Code        :", code)
print("8) Valid ID?   :", spy_id.startswith("AGENT") and code.isalpha())


"""
============================================================
  AB TUMHARI BAARI 🎯
  Neeche apne answers likho (upar ka code comment kar do
  ya naya cell jaisa samajhlo). Values badal badal ke khelo!
============================================================

  A) card = "9999-8888-7777-1111"  -> mask karo
  B) name = "Rahul123"            -> validator se check karo
  C) signal = "aXgXeXnXtX"        -> decode karo ([::2])
  D) phrase = "never odd or even" -> palindrome hai? (spaces pe dhyan)
  E) messy = "  pYtHoN iS fUn "   -> "Python Is Fun" banao

  Hint D ke liye: pehle .replace(" ", "") karo, phir compare.
"""
