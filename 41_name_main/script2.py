from script1 import *

# print(__name__)

def favoriteDrink(drink):
    print(f"My favorite drink is {drink}.")
    
def main():
    print("This is script2.py")
    favoriteFood("Sushi")
    favoriteDrink("Coffee")
    print("Goodbye!")

if __name__ == '__main__':
    main()