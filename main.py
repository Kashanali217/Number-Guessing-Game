import random

# Welcome Message
welcome_message = """Welcome to Number Guessing Game.
Created By Kashan Ali
"""
print(welcome_message.center(160))

# Telling Instructions of Game to user
instructions = """Instructions:
I've thinked of a random number in my mind.
You have to guess it in 7 Guesses.
If you guesss is lower than the original number i will say \"Higher Number Please!\" 
If you guesss is higher than the original number i will say \"Lower Number Please!\" 
If you will guess the number in 7 guesses you win
"""
print(instructions.title())

#  Random Number
random_number = random.randint(0, 100)

i = 0
while i < 7:
    i = i + 1
    user_input = int(input(f"Guess the Number.(Guess Number {i})"))
    if user_input > random_number:
        print("Lower Number Please!")
    elif user_input < random_number:
        print("Higher Number Please!")
    else:
        print(f"Congratulations! You Guessed it in {i} guesses. It was {random_number}")
        break
else:
    print(f"Sorry, you didn't guess the number. It was {random_number}.")