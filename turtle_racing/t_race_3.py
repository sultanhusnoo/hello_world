"""
	Create a set of 5 turtles and set them on a starting line. Turtles
	are created with a function.
"""
import turtle
import random

t_screen = turtle.Screen()

t=[]

def fn_create_turtles():
	for i in range(1,6):
		name = 't{}'.format(i)
		name = turtle.Turtle()
		t.append(name)	

def fn_startline():
	for my_turtle in t:
		my_turtle.penup()
		my_turtle.speed(1000)
		x_pos = -300 + (50 * (t.index(my_turtle)+1))
		my_turtle.goto(x_pos,-200)
		my_turtle.pendown()
		my_turtle.left(90)
		
fn_create_turtles()
fn_startline()
print(t)

#turtle.mainloop()
t_screen.exitonclick()
