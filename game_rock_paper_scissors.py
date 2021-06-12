#	Rock, Paper, Scissors Game
import random

options = ["Rock","Paper","Scissors"]
user_options = {"R":"Rock", "P":"Paper", "S":"Scissors"}

computer_score =0
user_score=0
count = 0

print("\n*********************************************")
print("Welcome to the game of Rock/Paper/Scissors.")
print("This if the Greatest game ever known to man!!")
print("...ohh and women also btw....")
print("...not to forget the kids also...")
print("Anyway, have fun and winner is best of three.")
print("*********************************************\n")

while(computer_score+user_score)!=3:
	computer_choice = random.choice(options)
	user_choice = str(input("Please input your choice (R/P/S) : "))
	user_choice = user_choice.upper()
	
	if user_choice=='' or (user_choice!="R" and user_choice!="P" and user_choice!="S"):
		print("Wrong input!")
		continue
	user_choice = user_options[user_choice]

	print("Your choice is    : {}".format(user_choice))
	print("Computer choice is: {}".format(computer_choice))

	if computer_choice==user_choice:
		print("You both selected '{}'. The match is a DRAW.\n".format(computer_choice))
	elif computer_choice=="Rock" and user_choice=="Paper":
		print("Paper beats Rock. You WIN!!\n")
		user_score+=1
	elif computer_choice=="Rock" and user_choice=="Scissors":
		print("Rock beats Scissors. Computer WINS!!\n")
		computer_score+=1
	elif computer_choice=="Paper" and user_choice=="Rock":
		print("Paper beats Rock. Computer WINS!!\n")
		computer_score+=1
	elif computer_choice=="Paper" and user_choice=="Scissors":
		print("Scissors beat Paper. You WIN!!\n")
		user_score+=1
	elif computer_choice=="Scissors" and user_choice=="Rock":
		print("Rock beats Scissors. You WIN!!\n")
		user_score+=1
	elif computer_choice=="Scissors" and user_choice=="Paper":
		print("Scissors beats Paper. Computer WINS!!\n")
		computer_score+=1
	count+=1

print("Computer: {}, You: {}".format(computer_score,user_score))
if computer_score>user_score:
	print("\nComputer WINS the game!!!")
else:
	print("\nCongratulations! You WIN!!!")
