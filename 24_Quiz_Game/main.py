questions = (
"What is the capital of India?",
"Which planet is known as the Red Planet?",
"What is 12 × 8?",
"Which language is primarily used to style web pages?",
"Who invented the light bulb?")

options = (
("A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"), 
("A. Earth", "B. Venus", "C. Mars", "D. Jupiter"), 
("A. 86", "B. 96", "C. 108", "D. 92"), 
("A. HTML", "B. Python", "C. CSS", "D. C++"), 
("A. Isaac Newton", "B. Albert Einstein", "C. Thomas Edison", "D. Nikola Tesla"))

answers = ("B", "C", "B", "C", "C")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
print("--------------------")
print("      RESULT        ")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")