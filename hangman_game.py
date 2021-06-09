#	Game written by HUSNOO M. Sultan on April 14th 2021
#	Hangman game. Computer will display a word with characters 
#	blanked out. User has to geuss characters to complete the word.

import random

def find_max_chances(word):
	singular_chars = {}
	for char in word:
		if char in singular_chars:
			singular_chars[char] += 1
		else:
			singular_chars[char] = 1
	return(len(singular_chars))

def display_word(word, correct_geusses):
	displayed_word = ''
	displayed_word += word[0]
	for char in word[1:-1]:
		if char in correct_geusses:
			displayed_word += char
		else:
			displayed_word += "_"
	displayed_word += word[-1]
	return displayed_word		
	
lst_words = [	"christmas","django","gear","cuisine","raptor","boy", 
				"robot","secret","game","island","children","bicycle",
				"hangmang","procrastinate","six"]

print("\n****************************************************")
print("Welcome to the game of HANGMAN! You know what to do.")
print("****************************************************")

while True:
	secret_word = random.choice(lst_words)

	correct_geusses = []
	user_geusses = []
	max_chances = find_max_chances(secret_word)
		
	print("\nThe secret word is: {}".format(display_word(secret_word,correct_geusses)))
	print("You have {} chances".format(max_chances))
	print("May the odds be ever in you favour!")

	while(len(user_geusses) < max_chances):
		user_geuss_input = str(input("\nPlease input your geuss for an alphabet in the word: "))
		if user_geuss_input in secret_word[1:-1]:
			correct_geusses.append(user_geuss_input)
			user_geusses.append(user_geuss_input)
			user_word = display_word(secret_word,correct_geusses)
			print(user_word)
		else:
			user_geusses.append(user_geuss_input)
			print("Wrong choice. Better luck next time MF!!")	
		if display_word(secret_word,correct_geusses) == secret_word:
			print("\nYou win MF!!")
			print("You correctly geussed the secret word '{}'".format(secret_word))
			break

	if display_word(secret_word,correct_geusses) != secret_word:
		print("\nYou fucking LOST!! You deceive me")
		print("Secret word was: {}".format(secret_word))		

	play_again_choice=str(input("Do you want to play again? (Y/N)  "))
	if play_again_choice.upper()=="N":
		break
	else:
		print("You chose to play again.")
		print("****************************************************")
		
print("\n****************************************************")
print("Farewell my friend. May your path stay safe!")
print("****************************************************")
