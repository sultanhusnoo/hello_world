"""
	Create a turtle and make it do some random moves, with random
	direction, random color, random distance at random speeds.
"""
import turtle
import random

t_screen = turtle.Screen()
sul = turtle.Turtle()

color_lst = ["red","blue","yellow","green","black"]

for i in range(0,50):
	t_speed = random.randint(0,100)
	t_distance = random.randint(0,5)
	t_angle = random.randint(0,360)
	t_direction = random.randint(0,1)
	my_pen_color = random.choice(color_lst)
	
	if t_direction == 0:
		sul.right(t_angle)
	elif t_direction ==1:
		sul.left(t_angle)
	
	sul.speed(t_speed)
	sul.pencolor(my_pen_color)
	sul.forward(t_distance)

#turtle.mainloop()
t_screen.exitonclick()
