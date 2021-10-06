import random

actions = ["Rock", "Paper", "Scissors"]
results = {'User': 0, 'Computer': 0}
game_invariant = 3

while results['User'] < 3 and results['Computer'] < 3:
	user_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors)\nYour turn: "))
	if user_choice in [1, 2, 3]:
		user_index = user_choice - 1
	else:
		print('Wrong choice!')
		continue

	computer_index = random.randint(0, game_invariant - 1)

	print(f"{actions[user_index]} vs. {actions[computer_index]}")

	if user_index == computer_index:
		print('Draw')
	elif user_index % game_invariant == 0 and computer_index % game_invariant == 2:
		results['User'] += 1
		print("User wins this round.")
	elif user_index % game_invariant == 2 and computer_index % game_invariant == 0:
		results['Computer'] += 1
		print("Computer wins this round.")
	elif user_index % game_invariant > computer_index % game_invariant:
		results['User'] += 1
		print("User wins this round.")
	else:
		results['Computer'] += 1
		print("Computer wins this round.")
	print(str(results['User'])+':'+str(results['Computer'])+'\n')

winner = 'User' if results['User'] >= results['Computer'] else 'Computer'
print(winner + ' wins!')
