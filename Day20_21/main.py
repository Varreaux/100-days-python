from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Morgan's Snake Game")
screen.tracer(0)
canvas = screen.getcanvas()
canvas.focus_force()

snake1 = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")




game_is_on = True
i = 0
while game_is_on:
    snake1.move()
    time.sleep(0.08)
    screen.update()

    pos = snake1.segments[0].pos()
    if pos[0]>=280 or pos[0]<=-280 or pos[1]<=-280 or pos[1]>=280 or snake1.collision():
        snake1.reset()
        score.reset(i)
        food.change_spot()
        i=0

    if snake1.segments[0].distance(food) < 15:
        food.change_spot()
        i+=1
        score.update(i)
        snake1.add_tail()
    

screen.exitonclick()
