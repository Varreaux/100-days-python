from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(1,5)
        self.penup()
        self.goto(x, y)

    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)
        

