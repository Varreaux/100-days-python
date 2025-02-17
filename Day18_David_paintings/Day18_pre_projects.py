from turtle import Turtle, Screen
from random import *

screen = Screen()
screen.colormode(255) 
root = screen.getcanvas().winfo_toplevel()
root.attributes('-topmost', 1)  # Bring to the front

timmy = Turtle()
timmy.shape("turtle")

def draw_shapes(angle_num):
    for shape_number in range(3, angle_num+1):
        timmy.pencolor((randint(0,255),randint(0,255),randint(0,255)))
        for _ in range(shape_number):
            timmy.right(360/shape_number)
            timmy.forward(100)


def rand_walk(number_of_steps):
    timmy.speed(0)
    timmy.pensize(10)
    for _ in range(number_of_steps):
        timmy.pencolor((randint(1,210),randint(1,210),randint(1,210)))
        direction = 90*(randint(1,4))
        timmy.left(direction)
        timmy.forward(20)


def spirograph(numOfCircles):
    for _ in range(numOfCircles):
        timmy.speed(0)
        timmy.pencolor((randint(1,210),randint(1,210),randint(1,210)))
        timmy.circle(100)
        timmy.left(360/numOfCircles)
        timmy.tilt(-360/numOfCircles)


spirograph(100)
        
    













screen.exitonclick()





