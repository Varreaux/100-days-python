from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list =[]
        self.step = STARTING_MOVE_DISTANCE
        self.chance = 30
        for _ in range(0, 10):
            self.new_car(True)

    def new_car(self, new):
        newcar = Turtle()
        newcar.color(random.choice(COLORS))
        newcar.shape("square")
        newcar.resizemode("user")
        newcar.setheading(180)
        newcar.shapesize(1,2)
        newcar.penup()
        if new:
            newcar.teleport(random.randint(-250, 280), random.randint(-250, 280))
        else: 
            newcar.teleport(280, random.randint(-250, 280))
        self.car_list.append(newcar)

    def move(self):
        for car in self.car_list:
            car.forward(self.step)
    
    def increase_speed(self):
            self.step+=MOVE_INCREMENT
            self.chance-=3

    def generate_new_car(self):
        x = random.randint(0,self.chance)
        if (x == 0):
            self.new_car(False)

    def collision(self, x, y):
        for car in self.car_list:
            if(car.distance(x,y)<=30 and (abs(y - car.ycor())<=21)):
                return True
        return False
    
    def erase(self, x, y):
        for car in self.car_list:
            if(car.distance(x,y)<=30 and (abs(y - car.ycor())<=21)):
                continue
            car.hideturtle()
        