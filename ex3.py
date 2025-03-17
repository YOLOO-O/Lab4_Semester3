# ex3.py - A guessing game where the user tries to guess a random number between 10 and 20

import random

# Generate a random number between 10 and 20
random_number = random.randint(10, 20)

# Prompt the user for input until they guess the correct number
while True:
    guess = int(input("Guess the number between 10 and 20: "))
    
    if guess == random_number:
        print("Congratulations! You've guessed the correct number.")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
