from random import random
from turtle import Turtle, Screen
import random

screen = Screen()
canvas = screen.getcanvas()
canvas.focus_force()
screen.setup(500, 400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
random.shuffle(colors)
for i in range(5):
    tim = Turtle(shape="turtle")
    tim.teleport(-130, -165 + (75*i))
    tim.color(colors[i])

screen.exitonclick()