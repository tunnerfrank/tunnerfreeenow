#ask the user for input on what they want btw rock, paper and scissors
#generate a random number using the module for the pc
#list the rock, paper, scissors into a list and split them
#create loops on accordance to the rules of the game
import random
print ("Welcome to ROCK, PAPER, SCISSORS GAME")
user_input = int(input("What do you choose (0 for ROCK)(1 for PAPER)(2 for SCISSORS)"))  
comp_number = random.randint(0, 2)
print(f"Computer chose {comp_number}")
game = ["rock", "paper", "scissors"]
if user_input == comp_number:
    print ("Draw")
    quit()
if user_input == 0 and comp_number == 2:
    print("YOU WIN")
    quit()
if user_input == 1 and comp_number == 0:
    print("YOU WIN")
    quit()
if user_input == 2 and comp_number == 1:
    print ("YOU WIN")
    quit()
if user_input < 0 or user_input > 2:
    print("invalid choice")
    quit()
else:
    print("YOU LOSE") 