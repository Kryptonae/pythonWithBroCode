import random

low = 1
high = 100
number = random.randint(low, high)
count = 0

while True:
    guess = input("Enter a number between 1 and 100: ")
    
    if guess.isdigit():
        guess = int(guess)
        if guess < low or guess > high:
            print(f"{guess} is out of range.")
            print(f"Please enter a number between {low} and {high}.")
            continue
        count += 1
    else:
        print("Invalid input. Please enter a valid number.")
        continue
    if guess > number:
        print(f"{guess} is too high. Try again.")
    elif guess < number:
        print(f"{guess} is too low. Try again.")
    else:
        print(f"Congratulations! {guess} is the correct number.")
        print(f"It took you {count} guesses.")
        break