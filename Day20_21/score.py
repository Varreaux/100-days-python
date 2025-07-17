from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.teleport(0,270)
        self.hideturtle()
        self.write("Score is 0", move=False, align='center', font=('Arial', 20, 'normal'))

        
    def final_screen(self,i):
        self.teleport(0,0)
        self.clear()
        self.color("Green")
        self.write(f"Final score is {i}\n Game Over", align='center', font=('Arial', 20, 'normal'))


    
