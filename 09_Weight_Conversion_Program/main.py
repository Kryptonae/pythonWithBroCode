# Python wight converter

weight = float(input("Enter your weight: "))

unit = input("kilograms or pounds? (K or L): ")

if unit == "K" or unit == "k":
    weight *= 2.205
    print(f"Weight: {round(weight, 3)}L")
elif unit == "L" or unit == "l":
    weight /= 2.205
    print(f"Weight: {round(weight, 3)}KG")
else: 
    print(f"{unit} was not valid")