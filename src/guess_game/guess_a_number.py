"""
Created on Fri Mar  2 02:37:32 2018

@author: kay
"""

import random

def the_game():
    guesses_made = 0
    name = raw_input('Hello! What is your name?\n') 
    number = random.randint(1, 20)
    print '\nAlright {0}, lets play a game. I am thinking of a number between 1 and 20.'.format(name)
    
    # keep requesting for a guess so long as user has not had 5 tries
    while guesses_made < 6:
        guess = int(raw_input('Take a guess: '))
        guesses_made += 1
        if guess < number:
            print 'Your guess is too low.\n'
        elif guess > number:
            print 'Your guess is too high.\n'
        else:
            break
    
    if guess == number:
        print 'Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made)
    else:
        print 'Nope. The number I was thinking of was {0}'.format(number)
        
the_game()
