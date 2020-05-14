"""
Created on Fri Mar  2 02:37:32 2018

@author: kay
"""

import random

def the_game():
    guesses_made = 0
    name = input("Hello! Enter your name: ") 
    number = random.randint(1, 20)
    print(f"\nAlright {name}, lets play a game. I am thinking of a number between 1 and 20.")
    
    # keep requesting for a guess so long as user has not had 5 tries
    while guesses_made < 6:
        guess = int(input("Take a guess: "))
        guesses_made += 1
        if guess < number:
            print("Your guess is too low.\n")
        elif guess > number:
            print("Your guess is too high.\n")
        else:
            break
    
    if guess == number:
        print(f"Good job, {name}! You guessed my number in {guesses_made} guesses!")
    else:
        print(f"Nope. The number I was thinking of was {number}")
        
the_game()
