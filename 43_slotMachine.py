def spinRow():
    pass

def printRow():
    pass

def getPayout():
    pass

def main():
    print("***************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍋 🍊 🍉 💎")
    print("***************************")
    
    isRunning = True
    balance = 100  # Starting balance for the player
    symbols = [
        "🍒",
        "🍋",
        "🍊",
        "🍉",
        "💎"
    ]
    
    while isRunning:
        print(f"Current balance: ${balance:.2f}")
        try:
            bet = float(input("Place your bet Amount: $"))
        except ValueError:
            print("Invalid Amount. Please enter a valid Amount.")
        print("Spinning...")
        print("***************************")
        print("***************************")
        
    
        

if __name__ == '__main__':
    main()