"""
	Create a set of turtles and set them on a starting line. Turtles
	are individually created.
"""
import turtle
import random

t_screen = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t = [t1,t2,t3,t4,t5]

def fn_startline():
	for my_turtle in t:
		my_turtle.penup()
		my_turtle.speed(1000)
		x_pos = -300 + (50 * (t.index(my_turtle)+1))
		my_turtle.goto(x_pos,-200)
		my_turtle.pendown()
		my_turtle.left(90)
		
fn_startline()

#turtle.mainloop()
t_screen.exitonclick()
