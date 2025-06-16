from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        x = y = 0
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.teleport(x, y)
            new_segment.penup()
            self.segments.append(new_segment)
            x-=20

    def add_tail(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        self.segments.append(new_segment)

    def collision(self):
        for seg in self.segments[1:]:
            if self.segments[0].distance(seg)<15:
                return True
        return False
            


    
    def move(self):
            for seg_num in range(len(self.segments)-1, 0, -1):
                new_x = self.segments[seg_num-1].xcor()
                new_y = self.segments[seg_num-1].ycor()
                self.segments[seg_num].teleport(new_x,new_y)
            self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
         if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)