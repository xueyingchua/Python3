## AUTOMATED ROCK PAPER SCISSORS GAME
# Creating a game where the outcome is automatically chosen for both players.
# The number of times the game is played can be adjusted.
# Xue Ying Chua 2020
#_____________________________________________________________________________
import random # random number generator
#import numpy as np
#import array

choice = ['rock', 'paper', 'scissors'] # the three choices in the game [0,1,2]

n_play = 3 # number of times the game is played

P1_choice_tot = [0]*n_play # empty matrix to store P1 choices
P2_choice_tot = [0]*n_play # empty matrix to store P2 choices
P1_wins = [0]*n_play # empty matrix to store P1 wins
P2_wins = [0]*n_play # empty matrix to store P2 wins

for x in range(0, n_play): 
    
    # Show the current round
    print(f'Round number : {x}')    

    # Selecting an option for Player 1
    rand_num = random.randint(0,2) # randomly selecting a number from 0,1,2
    P1_choice_tot[x] = rand_num # storing the choices as a number first
    P1_choice = choice[rand_num] # using the randomly selected number to make a choice
    print(f'P1: {P1_choice}') # printing Player 1's choice
    
    # Selecting an option for Player 2
    rand_num = random.randint(0,2)
    P2_choice_tot[x] = rand_num
    P2_choice = choice[rand_num]
    print(f'P2: {P2_choice}')
        
    # Conditional statements for winning
    if P1_choice == P2_choice: # if both players make the same choice
        print('Draw!') # no wins for each player
    
    elif P1_choice == 'paper' and P2_choice == 'rock':
        print('P1 wins!')
        P1_wins[x] = 1 # storing P1 wins
    
    elif P1_choice == 'rock' and P2_choice == 'scissors':
        print('P1 wins!')
        P1_wins[x] = 1 
    
    elif P1_choice == 'scissors' and P2_choice == 'paper':
        print('P1 wins!')
        P1_wins[x] = 1 
    
    else:
        print('P2 wins!')
        P2_wins[x] = 1 # storing P2 wins

# Generate a bar chart to show how many times rock, scissors, and paper was chosen by each player



