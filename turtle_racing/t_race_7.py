"""
	A set of turtles are made to race. 
	User sets number of turtles to beracing.
	User can place a bet on a turtle to win.
"""
import turtle
import random
import tkinter as tk
from tkinter import messagebox as mb

color_lst = ["red","blue","yellow","green","violet","gold",
			"orange", "magenta"]

def fn_start_finish_line():
	#	Set width of track for number of turtles racing
	width = (num_t * 50) + 50
	
	#	Create turtle that will draw start/finish lines
	my_line = turtle.Turtle()
	my_line.color("white")
	my_line.speed(1000)
	my_line.hideturtle()
	
	#	Draw start line
	my_line.penup()
	my_line.goto(-300,-200)
	my_line.pendown()
	my_line.forward(width)

	#	Draw finish line
	my_line.penup()
	my_line.goto(-300,200)
	my_line.pendown()
	my_line.forward(width)

def fn_create_turtles(num_t):
	for i in range(1,(num_t+1)):
		name = 't{}'.format(i)
		name = turtle.Turtle()
		t.append(name)
		name.color(random.choice(color_lst))

def fn_startline():
	for my_turtle in t:
		my_turtle.penup()
		my_turtle.speed(1000)
		x_pos = -300 + (50 * (t.index(my_turtle)+1))
		my_turtle.goto(x_pos,-200)
		my_turtle.pendown()
		my_turtle.left(90)
		my_turtle.write("T{}".format(t.index(my_turtle)+1), move=False,
							font=('times new roman',15,'bold'))

def fn_move_forward():	#	Move turtle ahead by a random distance at 
	while (True):		#	a random speed
		for item in t:
			dist = random.randint(0,100)
			item.speed(random.randint(0,1000))
			item.forward(dist)
			if (item.ycor() >= 200):	# Check if winner
				winner_name = "{}".format(t.index(item)+1)
				fn_announce_winner(winner_name)
				return None

scores=[]	#	Empty list to store players wins and losses
def fn_announce_winner(my_winner):
	root = tk.Tk()
	root.withdraw()
	if user_bet == my_winner:
		conclu = "You WIN!!!"
		scores.append("WIN")
		print("Win")
	else:
		conclu = "You LOSE!!!"
		scores.append("LOSS")
		print("Loss")
	my_msg = "Winner is Turtle: T{}! \n{}".format(my_winner, conclu)
	tk.messagebox.showinfo(title="Turtle Racing", message = my_msg)
	
def print_scores():	
	num_match = len(scores)
	num_win = scores.count("WIN") 
	num_loss = scores.count("LOSS") 
	per_win = 100 * (num_win / num_match)
	per_loss = 100 * (num_loss / num_match)
	print("\n\n**********************************")
	print("You played {} matche(s).".format(num_match))
	print("You Won {} matche(s). ({:.1f}%)".format(num_win, per_win))
	print("You Lost {} matche(s). ({:.1f}%)".format(num_loss, per_loss))
	print("**********************************")
	if num_win > num_loss:
		print("\nYOU WIN!!")	
	elif num_win < num_loss:
		print("\nYOU LOSE!!")
	elif num_win == num_loss:
		print("\nIts a DRAW! :( ")
		
while True:
	num_t = int(input("\nPlease input the number of turtles to race: "))
	user_bet = str(input("Place a bet on the winning Turtle: T"))

	t = []	#	list of turtles to be racing
	t_screen = turtle.Screen()
	t_screen.clear()
	t_screen.bgcolor("black")		

	fn_create_turtles(num_t)
	fn_start_finish_line()
	fn_startline()
	fn_move_forward()
	
	user_choice = input("\nDo you want to Quit (Y/N)? ")
	if user_choice.upper() == "Y":
		break

print_scores()
t_screen.exitonclick()
