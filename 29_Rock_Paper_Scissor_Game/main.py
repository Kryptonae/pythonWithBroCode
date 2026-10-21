import random

options = ("rock", "paper", "scissor")
isRunning = True
userScore = 0
computerScore = 0

while isRunning:
    
    userChoice = input("Enter Rock, Paper or Scissors (or 'q' to quit): ").lower()
    if userChoice != "rock" and userChoice != "paper" and userChoice != "scissor" and userChoice != "q":
        print("Invalid input. Please enter Rock, Paper, Scissors or 'q' to quit.")
        continue
    
    computerChoice = random.choice(options)

    if userChoice == 'q':
        print(f"Final Score: You {userScore} - Computer {computerScore}")
        if userScore > computerScore:
            print(f"Congratulations! You won the game with a score of {userScore} to {computerScore}.")
        elif userScore < computerScore:
            print(f"Sorry! You lost the game with a score of {userScore} to {computerScore}.")
        else:
            print(f"The game ended in a tie with a score of {userScore} to {computerScore}.")
        break
    elif userChoice == computerChoice:
        print(f"Computer chose {computerChoice} You chose {userChoice}. It's a tie!", end="")
        print()
        print(f"Score: You {userScore} - Computer {computerScore}")
    elif userChoice == "rock" and computerChoice == "scissor":
        userScore += 1
        print(f"Computer chose {computerChoice} You chose {userChoice}. You win!", end="")
        print()
        print(f"Score: You {userScore} - Computer {computerScore}")
    elif userChoice == "paper" and computerChoice == "rock":
        userScore += 1
        print(f"Computer chose {computerChoice} You chose {userChoice}. You win!", end="")
        print()
        print(f"Score: You {userScore} - Computer {computerScore}")
    elif userChoice == "scissor" and computerChoice == "paper":
        userScore += 1
        print(f"Computer chose {computerChoice} You chose {userChoice}. You win!", end="")
        print()
        print(f"Score: You {userScore} - Computer {computerScore}")
    else:
        computerScore += 1
        print(f"Computer chose {computerChoice} You chose {userChoice}. You lose!", end="")
        print()
        print(f"Score: You {userScore} - Computer {computerScore}")