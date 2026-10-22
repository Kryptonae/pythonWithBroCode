def showBalance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def showDeposit():
    try:
        depositeAmount = float(input("Enter the amount to deposit: $"))
    except ValueError:
        print("Deposit amount must be a number. Please try again.")
        return 0
    
    if depositeAmount < 0:
        print("Deposit amount cannot be negative. Please try again.")
        return 0
    else:
        return depositeAmount

def showWithdraw():
    try:
        withdrawAmount = float(input("Enter the amount to withdraw: $"))
    except ValueError:
        print("Withdraw amount must be a number. Please try again.")
        return 0

    if withdrawAmount < 0:
        print("Withdraw amount cannot be negative. Please try again.")
        return 0
    else:
        return withdrawAmount

balance = 0
isRunning = True

while isRunning:
    print("****************************************")
    print("Welcome to the Banking Program".center(40))
    print("****************************************")

    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    print("****************************************")

    choice = input("Enter your choice (1-4): ")
    
    match choice:
        case '1':
            showBalance(balance)
        case '2':
            balance += showDeposit()
        case '3':
            balance -= showWithdraw()
        case '4':
            isRunning = False
            print("Thank you for using the Banking Program. Goodbye!")
        case _:
            print("Invalid choice. Please try again.")
    
    print("****************************************")