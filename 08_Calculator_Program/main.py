# Calculator Program

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2;
    print(f"Result: {round(result , 3)}")
elif operator == "-":
    result = num1 - num2;
    print(f"Result: {round(result , 3)}")
elif operator == "*":
    result = num1 * num2;
    print(f"Result: {round(result , 3)}")
elif operator == "/":
    if num2 == 0:
        print("Divide by 0 is not possible")
    else: 
        result = num1 / num2
        print(f"Result: {round(result , 3)}")
else:
    print(f"{operator} is not a Invalid Operator")