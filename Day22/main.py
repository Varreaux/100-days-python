from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import random

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("morgan's pong game")
canva = screen.getcanvas()
canva.focus_force()

screen.tracer(0)
rightpaddle = Paddle(350,0)
leftpaddle = Paddle(-350,0)
# screen.tracer(1)

screen.listen()
screen.onkey(rightpaddle.up, "Up")
screen.onkey(rightpaddle.down, "Down")

screen.onkey(leftpaddle.up,"w")
screen.onkey(leftpaddle.down, "s")

ball = Ball()

game_over =False
x=5
y=0
score1 = Score(-150, 200)
score2 = Score(+150, 200)
while(not game_over):
    screen.update()
    ball.move(x,y)
    if(ball.ycor()>285 or ball.ycor()<-285):
        y = -y
    if((ball.distance(rightpaddle)<50 and ball.xcor()>330) 
       or (ball.distance(leftpaddle)<50 and ball.xcor()<-330)):
        x= -x
    if(ball.xcor()>380 or ball.xcor()<-380):
        y = 0
        while y == 0:
            y = random.randint(-5,5)
        x = random.randint(-5,-3)
        if(ball.xcor()<0):
            x = -x
            score1.increaseScore()
        else:
            score2.increaseScore()
        ball.goto(0,0)



screen.exitonclick()

