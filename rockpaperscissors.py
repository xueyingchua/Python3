## AUTOMATED ROCK PAPER SCISSORS GAME
# Creating a game where the outcome is automatically chosen for both players.
# The number of times the game is played can be adjusted.
# This code also analyses how many times a choice was made by each player and how many wins each player has.
# Xue Ying Chua 2020
#_____________________________________________________________________________
import random # random number generator
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

choice = ['rock', 'paper', 'scissors'] # the three choices in the game

n_play = 30 # number of times the game is played

P1_choice_tot = [0]*n_play # empty matrix to store P1 choices
P2_choice_tot = [0]*n_play # empty matrix to store P2 choices
P1_wins = [0]*n_play # empty matrix to store P1 wins
P2_wins = [0]*n_play # empty matrix to store P2 wins

for x in range(0, n_play): 
    
    # Show the current round
    print(f'Round number : {x}')    

    # Selecting an option for Player 1
    rand_num = random.randint(0,2) # randomly selecting a number from 0,1,2
    P1_choice = choice[rand_num] # using the randomly selected number to make a choice
    P1_choice_tot[x] = P1_choice # storing the choices    
    print(f'P1: {P1_choice}') # printing Player 1's choice
    
    # Selecting an option for Player 2
    rand_num = random.randint(0,2)
    P2_choice = choice[rand_num]
    P2_choice_tot[x] = P2_choice    
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

# Listing out the number of times rock, paper, and scissors appeared for each player
P1_choice_list = [P1_choice_tot.count('rock'), P1_choice_tot.count('paper'), P1_choice_tot.count('scissors')]
P2_choice_list = [P2_choice_tot.count('rock'), P2_choice_tot.count('paper'), P2_choice_tot.count('scissors')]

# Generate a bar chart to show how many times rock, scissors, and paper was chosen by each player
label_loc = np.arange(len(choice)) # the label locations
width = 0.35  # the width of the bars

# settings for the bar plot
fig, ax = plt.subplots()
rects1 = ax.bar(label_loc - width/2, P1_choice_list, width, label='Player 1', color=['red'])
rects2 = ax.bar(label_loc + width/2, P2_choice_list, width, label='Player 2', color=['blue'])

ax.set_title('Number of times each choice was made') # figure title
ax.set_ylabel('Counts') # y label
ax.set_xlabel('Choices') # x label
ax.set_xticks(label_loc) # location for x axis labels
ax.set_xticklabels(choice) # x axis labels
ax.legend() # figure legend

# Showing the bar plot
fig.tight_layout()
plt.show()

# Counting how many times each player won the game
P1_wins_tot = sum(P1_wins)
P2_wins_tot = sum(P2_wins)

# Summary of all the wins and number of games played
game_summary = [P1_wins_tot, P2_wins_tot, n_play]
game_summary_label = ['P1 wins', 'P2 wins', 'Number of games']

# Plotting a horizontal bar chart
plt.rcdefaults()
fig, ax = plt.subplots()

y_pos = np.arange(len(game_summary)) # the label locations
ax.barh(y_pos, game_summary, width, color=['black']) 
ax.set_title('Game summary') # figure title
ax.set_xlabel('Counts') # x label
ax.set_yticks(y_pos) # location for y axis labels
ax.set_yticklabels(game_summary_label) # y axis labels

plt.show()