# print(dir())
# print(__name__)

# from script2 import *

# if __name__ == '__main__':
#     main()

# print(__name__)

def favoriteFood(food):
    print(f"My favorite food is {food}.")

def main():
    print("This is script1.py")
    favoriteFood("Pizza")
    print("Goodbye!")
    
if __name__ == '__main__':
    main()