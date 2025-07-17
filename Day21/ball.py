from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        self.setheading(50)

    def move(self,x,y):
        # self.forward(5)
        new_x = self.xcor()+x
        new_y = self.ycor()+y
        self.goto(new_x,new_y)


