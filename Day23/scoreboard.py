from turtle import Turtle
FONT = ("Courier", 24, "normal")
END_FONT = ("Courier", 35, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.teleport(-230, 250)
        self.hideturtle()
        self.write((f"Level {self.score}"),False,"center", FONT)

    def increase_counter(self):
        self.score+=1
        self.clear()
        self.write((f"Level {self.score}"),False,"center", FONT)

    def game_over(self):
        self.clear()
        self.teleport(0, 0)
        self.write("Game Over",False,"center", END_FONT)
        self.teleport(0, -20)
        self.write((f"Level {self.score}"),False,"center", FONT)
