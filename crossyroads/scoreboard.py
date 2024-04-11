from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.level = 1
        self.score_write()


    def game_over(self):
        self.goto(0,0)
        self.write("Game over...", align="center", font=FONT)

    def increase_lvl(self):
        self.level +=1
        self.score_write()
    def score_write(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)