from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Morgan's Snake Game")
screen.tracer(0)
canvas = screen.getcanvas()
canvas.focus_force()

snake1 = Snake()

screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")





game_is_on = True
while game_is_on:
    snake1.move()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
