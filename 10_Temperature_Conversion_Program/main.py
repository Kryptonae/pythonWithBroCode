# Temperature Conversion Program

unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")

temp = float(input("Enter the temperature: "))

if unit == "C" or unit == "c":
    temp = round((temp * (9 / 5) + 32), 3)
    print(f"Temperature: {temp}°F")
elif unit == "F" or unit == "f":
    temp = round(((temp - 32) * 5 / 9), 3)
    print(f"Temperature: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")