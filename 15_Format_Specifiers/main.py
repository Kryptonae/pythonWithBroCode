""" FORMAT SPECIFIERS = {:FLAGS} FORMAT A VALUE BASED ON WHAT FLAGS ARE INSERTED

.(NUMBER)F = ROUND TO THAT MANY DECIMAL PLACES (FIXED POINT)
:(NUMBER) = ALLOCATE THAT MANY SPACES
:03 = ALLOCATE AND ZERO PAD THAT MANY SPACES
:< = LEFT JUSTIFY
:> = RIGHT JUSTIFY
:^ = CENTER ALIGN
:+ = USE A PLUS ISGN TO INDICATE POSITIVE VALUE
:= = PLACE SIGN TO LEFTMOST POSITION
: = INSERT A SPACE BEFORE POSITIVE NUMBERS
:, = COMMA SEPRATOR

 """
 
price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# print(f"Price 1 is ${price1:.1f}")
# print(f"Price 2 is ${price2:.1f}")
# print(f"Price 3 is ${price3:.1f}")

# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}")

# print(f"Price 1 is ${price1:<10}")
# print(f"Price 2 is ${price2:<10}")
# print(f"Price 3 is ${price3:<10}")

# print(f"Price 1 is ${price1:>10}")
# print(f"Price 2 is ${price2:>10}")
# print(f"Price 3 is ${price3:>10}")

# print(f"Price 1 is ${price1:^10}")
# print(f"Price 2 is ${price2:^10}")
# print(f"Price 3 is ${price3:^10}")

# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")

# print(f"Price 1 is ${price1: }")
# print(f"Price 2 is ${price2: }")
# print(f"Price 3 is ${price3: }")

# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}")

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:,.2f}")
print(f"Price 3 is ${price3:,.2f}")