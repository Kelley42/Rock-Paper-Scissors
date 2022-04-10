import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Defs
def print_userchoice(userchoice):
	global rock, paper, scissors
	if userchoice == "rock":
		print(rock)
	elif userchoice == "paper":
		print(paper)
	elif userchoice == "scissors":
		print(scissors)
	else:
		print("\nIncorrect choice - try again!")
		game()


def print_computerchoice(computerchoice):
	if computerchoice == "rock":
		print(f"Computer chooses: rock{rock}")
	elif computerchoice == "paper":
		print(f"Computer chooses: paper{paper}")
	elif computerchoice == "scissors":
		print(f"Computer chooses: scissors{scissors}")


def playagain():
	question = input("\nPlay again? ").lower()

	questionyes = ["yes", "y"]
	questionno = ["no", "n"]
	
	if any(match in question for match in questionyes):
		game()
	elif any(match in question for match in questionno):
		exit()
	else:
		print("\nIncorrect response - try again!")
		playagain()

		
def game():
    userchoice = input("\nWhat do you choose? Rock, paper, or scissors? ").strip(" ").lower()
    print_userchoice(userchoice)

    seq = ["rock", "paper", "scissors"]
    computerchoice = random.choice(seq)
    print_computerchoice(computerchoice)
    
    row1 = ["It's a draw", "You lose", "You win"]
    row2 = ["You win", "It's a draw", "You lose"]
    row3 = ["You lose", "You win", "It's a draw"]
    grid = [row1, row2, row3]

    y = int(seq.index(computerchoice))
    x = int(seq.index(userchoice))
    print(grid[x][y])

    playagain()
			
# Start game
print("Rock Paper Scissors Game!")

game()

