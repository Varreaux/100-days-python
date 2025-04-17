from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def go_forward():
    tim.forward(10)
def go_backward():
    tim.backward(10)
def go_left():
    tim.left(5)
def go_right():
    tim.right(5)
def clear():
    screen.resetscreen()

screen.listen()
screen.onkeypress(go_forward, "w")
screen.onkeypress(go_backward, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeypress(clear, "c")


screen.exitonclick()
