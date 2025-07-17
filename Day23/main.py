import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("morgan's turle crossing :)")
screen.tracer(0)
screen.bgcolor("black")
canvas = screen.getcanvas()
canvas.focus_force()

level = Scoreboard()
bob = Player()
cars = CarManager()

screen.listen()
screen.onkey(bob.move, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    cars.generate_new_car()
    if (bob.reached_end()):
        level.increase_counter()
        cars.increase_speed() 
    cars.move()
    if cars.collision(bob.xcor(),bob.ycor()):
        game_is_on = False
    screen.update()

level.game_over()
cars.erase(bob.xcor(),bob.ycor())
screen.update()


screen.exitonclick()

