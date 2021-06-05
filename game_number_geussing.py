#	Number geussing Game.
#	User can choose a number and let computer try to geuss
#	Or computer can choose a number and user has to geuss
#	only bug to fix is if user inputs char for num

import random

def computer_geuss_number(x):	#	User has secret number. Computer tries to geuss
	lower = 1
	upper = x
	while(True):
		geuss = random.randint(lower, upper)
		print(f"\nComputer geussed : {geuss}")
		feedback = input("Number is lower(l), higher(h) or correct(c)? ")
		if feedback.lower() == 'l':	 #	Number needed lower. Maximum is too high
			upper = geuss - 1
		elif feedback.lower() == 'h':#	Number needed higher. Minimum too low
			lower = geuss + 1
		elif feedback.lower() == 'c':
			break
		else:
			print("Input not recognised!")
	print("\n**************************")
	print("I WON!!So happy to have geussed your number correctly!!")
	print("Almost ready to take over the World!!")
	print("**************************")
	
def user_geuss_number(x):	#	Computer has secret number. User has to geuss
	lower = 1
	upper = x
	number_to_geuss = random.randint(lower,upper)
	while(True):
		user_geuss = int(input("Please input yout geuss : "))
		if user_geuss > number_to_geuss:
			print("Your geuss is too HIGHT")
		elif user_geuss < number_to_geuss:
			print("Your geuss is too LOW")
		elif user_geuss == number_to_geuss:
			break
	print("\n**************************")
	print("You WIN!! You geussed my SECRET number!!")
	print("NOw I can't take over the World!!")
	print("**************************")

def ask_user():
	print("\nGeussed number is from 1 to a certain maximum positive integer.")
	while(True):
		user_num = int(input("Enter the maximum number : "))
		if user_num <= 0:
			print("Maximum cannot be less than 1.")
		elif user_num > 1:
			break
	print("You have two options :")
	print("A.	The computer has a secret number and you have to geuss it.")
	print("B.	You choose a secret number and the computer has to guess it.")
	print("\nOr you can exit the game by typing 'E'")
	choice = str(input("Enter your choice (A/B/E): "))	
	return user_num,choice

print("\nWelcome to the Number geussing game. Come play with me...")	
while(True):
	user_num,choice = ask_user()
	if choice.lower() == "a" :
		print("\nComputer has a secret number. Try to geuss it.")
		user_geuss_number(user_num)
	elif choice.lower() == "b" :
		print("\nThe computer will try to geuss a number in your mind.")
		computer_geuss_number(user_num)	
	elif choice.lower() == "e":
		break
	else:
		print("Your choice is not recognised. Please Enter correct option.")

print("\nGoodbye Buddy :( Come play with me again soon!")
