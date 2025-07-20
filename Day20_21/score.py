from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        with open("Day20_21/hscore.txt", "r") as file:
            self.highscore = file.read()
        self.teleport(0,270)
        self.hideturtle()
        self.reset(0)

    def reset(self, i):
        self.clear()
        if i > int(self.highscore):
            with open("Day20_21/hscore.txt","w") as file:
                file.write(str(i))
            self.highscore = str(i)
        self.write(f"Score is 0; High Score is {self.highscore}", align='center', font=('Arial', 20, 'normal'))
        
    def update(self,i):
        self.clear()
        self.write(f"Score is {i}; High Score is {self.highscore}", align='center', font=('Arial', 20, 'normal'))


    
