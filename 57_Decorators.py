def addSprinkles(func):
    def wrapper():
        print("Adding sprinkles to your ice cream...")
        func()
    return wrapper

@addSprinkles
def getIceCream():
    print("Here is your ice cream!")
    
getIceCream()