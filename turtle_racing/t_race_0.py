"""
	Generate a Turtle and make it do some random stuff.
"""
import turtle
import random

t_screen = turtle.Screen()

sul = turtle.Turtle()

for i in range(0,10):
	t_distance = random.randint(0,50)
	t_angle = random.randint(0,360)
	t_direction = random.randint(0,1)
	
	if t_direction == 0:
		sul.right(t_angle)
	elif t_direction ==1:
		sul.left(t_angle)
	
	sul.forward(t_distance)

#turtle.mainloop()
t_screen.exitonclick()
