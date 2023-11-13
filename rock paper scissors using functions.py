#rock, paper, scissors game
#ask the user to give a input on what he wants
#let the user generate a random number considering a list of rock paper scissors
import random
choice = input("CHOOSE: ROCK, PAPER, SCISSORS").upper()
comp_choice = ["ROCK", "PAPER", "SCISSORS"]
random_choice = random.choice(comp_choice)
print(f"Computer chose {random_choice}")
def game(choice, random_choice):
    if choice == "ROCK" and random_choice == "SCISSORS":
        print("you win")
        quit()
    if choice == "PAPER" and random_choice == "ROCK":
        print("you win")
        quit()
    if choice == "SCISSORS" and random_choice == "PAPER":
        print("you win")
        quit()
    if choice == random_choice:
        print("draw")
        quit()
    else:
        print("you lose")
game(choice, random_choice)
cont = input("would you like to play again?")
while cont == "yes":
    choice = input("CHOOSE: ROCK, PAPER, SCISSORS").upper()
    comp_choice = ["ROCK", "PAPER", "SCISSORS"]
    random_choice = random.choice(comp_choice)
    print(f"Computer chose {random_choice}")
    game(choice, random_choice)
    cont = input("would you like to play again?")
if cont == "no":
    print("goodbye")