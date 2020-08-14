# Automated rock paper scissors game
import random

choice = ['rock', 'paper', 'scissors']

# Selecting an option for Player 1
rand_num = random.randint(0,2) #randomly selecting a number from 0,1,2
P1_choice = choice[rand_num] #using the randomly selected number to make a choice
print(f'P1: {P1_choice}') #printing Player 1's choice

# Selecting an option for Player 2
rand_num = random.randint(0,2)
P2_choice = choice[rand_num]
print(f'P2: {P2_choice}')

# Conditional statements for winning
if P1_choice == P2_choice: #if both players make the same choice
	print('Draw')
elif P1_choice == 'paper' and P2_choice == 'rock':
	print('P1 wins')
elif P1_choice == 'rock' and P2_choice == 'scissors':
	print('P1 wins')
elif P1_choice == 'scissors' and P2_choice == 'paper':
	print('P1 wins')
else:
	print('P2 wins')

