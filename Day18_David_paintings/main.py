from turtle import Turtle, Screen
from random import choice
import colorgram

screen = Screen()
screen.colormode(255) 
root = screen.getcanvas().winfo_toplevel()
root.attributes('-topmost', 1)

tim = Turtle()

colors = colorgram.extract("Day18_David_paintings/image.jpg", 100)

y = 0.00
tim.speed("fastest")
tim.penup()
tim.hideturtle()

for _ in range(10):
    for _ in range(10):
        tim.dot(15,choice(colors).rgb)
        tim.forward(30)
    y += 30
    tim.teleport(0, y)


screen.exitonclick()
