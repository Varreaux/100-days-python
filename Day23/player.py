from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.teleport(*STARTING_POSITION)
        self.setheading(90)
        self.penup()
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reached_end(self):
        if(self.ycor() >= FINISH_LINE_Y):
           self.teleport(*STARTING_POSITION)
           return True
        return False
            

        
