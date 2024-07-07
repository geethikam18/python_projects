from day12_guess_number_logo import logo

print(logo)

import random

from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5




#Function to check user guess against actual guess.

def check(guess, ans):
    if guess > ans:
        if guess - ans <= 10:
            print("High, but you're close!")
        else:
            print("Too high.")
    elif guess < ans:
        if guess - ans <= 10:
            print("Low, but you're close!")
        else:
            print("Too low.")
    else:
        print("You got it! The answer was {ans}.")


# Make function to set difficulty.

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():

    # Computer chooses a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")
    ans = randint(1, 100)

    #print(f"The correct answer is {ans}")

    # User chooses difficulty

    turns = difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")


    # Repeat the guessing til the attempts get over

    guess = 0
    while guess != ans and turns > 0:

        # User guess a number.
        guess = int(input("Make a guess: "))
        check(guess, ans)
        turns -= 1

        if guess != ans:
            print(f"You have {turns} attempts remaining to guess the number.")
        if turns == 0 and guess != ans:
            print("You've run out of guess, You lose.")
            return
        
game()



