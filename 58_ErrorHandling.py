while True:
    try:
        number = int(input("Enter a Number: "))
        print(f"{1 / number:.2f}")  # This will raise a ZeroDivisionError if number is 0
    except ValueError:
        print("Invalid input!")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception:
        print("Something went wrong!")
    else:
        print(f"You entered: {number}")
        break
    finally:
        print("Do some Cleanup Here!")