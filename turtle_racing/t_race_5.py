"""
	Create a set of turtles and set them on a starting line. Turtles
	are created with a function. User sets number of turtles to be 
	created. Each turtle is a different random color. Turtles race 
	to finish line.
"""
import turtle
import random

num_t = int(input("Please input the number of turtles desired: "))

t_screen = turtle.Screen()
color_lst = ["red","blue","yellow","green","black","violet","gold",
			"orange", "magenta"]

t=[]

def fn_start_finish_line():
	#	Set width of track for number of turtles racing
	width = (num_t * 50) + 50
	
	#	Create turtle that will draw start/finish lines
	my_line = turtle.Turtle()
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

def fn_move_forward():
	while (True):
		for item in t:
			dist = random.randint(0,10)
			item.speed(random.randint(0,1000))
			item.forward(dist)
			if (item.ycor() >= 200):	# Check if winner
				winner_name = "{}".format(t.index(item)+1)
				print("We have a winner: Turtle 't{}'!!".format(winner_name))
				return None
		
fn_create_turtles(num_t)
fn_start_finish_line()
fn_startline()
fn_move_forward()

#turtle.mainloop()
t_screen.exitonclick()
