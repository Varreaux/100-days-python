from turtle import Turtle


class Score(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.teleport(x,y)
        self.count = 0
        self.write(self.count, align="center", font=('Arial', 80, 'normal'))


    def increaseScore(self):
        self.clear()
        self.count+=1
        self.write(self.count, align="center", font=('Arial', 80, 'normal'))


