from turtle import Turtle
import random

class Food (Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.change_spot()

    
    def change_spot(self):
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 270)
        self.teleport(rand_x, rand_y)