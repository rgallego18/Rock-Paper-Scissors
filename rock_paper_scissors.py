#Update 1.2

import time
import random

print ("Hello! Welcome to rock paper scissors!")
print ("First, you will either choose - rock, paper, or scissors\nThen, the computer will randomly choose a choice")
 
time.sleep(3.0)

def beginning():
    global choice
    global a
    choice = input("Please choose a choice. Type here: ")
    options = ["Rock", "Paper", "Scissors"]
    a = (random.choice(options))
    print ("You chose: ",choice)
    print ("The computer chose: ",a)


def rankings():
    if choice == "rock" and a == "Paper":
        print ("Computer Wins!")
    elif choice == "rock" and a == "Scissors":
        print ("You win!")
    elif choice == "paper" and a == "Rock":
        print ("You win!")
    elif choice == "paper" and a == "Scissors":
        print ("Computer Wins!")
    elif choice == "scissors" and a == "Rock":
        print ("Computer Wins!")
    elif choice == "scissors" and a == "Paper":
        print ("You win!")
    else:
        print ("It's a tie!")                          

beginning()
rankings()
def infinite():    
    replay = input("Would you like to play again? Type here: ")
    if replay == "Yes" or replay == "yes":
        beginning()
        rankings()
        infinite() 
    elif replay == "No" or replay == "no":
        print ("Ok!")
    else:
        print ("Please try again")     

infinite()