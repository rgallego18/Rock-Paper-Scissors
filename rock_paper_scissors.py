import time
import random

#first 2 print statements are just introductions and rules
print ("Hello! Welcome to rock paper scissors!")
print ("First, you will either choose - rock, paper, or scissors\n Then, the computer will randomly choose a choice (trust me it is random)")

#gives user time to read the intro and then automatically starts the game 
time.sleep(0.5)

choice = input("Please choose a choice. Type here: ")
options = ["Rock", "Paper", "Scissors"]

#Stores the random choice in the variable "a"
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

rankings()

#This project is subject to future updates!! These include (but not limited to): 
#Adding a replay feature
#Canceling the round if you spell something wrong
#Adding rock paper scissors lizard spock