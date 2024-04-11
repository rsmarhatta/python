from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.sety(260)

        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def addpoints(self):
        self.score += 1
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align =ALIGNMENT, font=FONT)

    # def gameover(self):
    #     self.sety(0)
    #     self.write("Game over.", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("highscore.txt", mode="w") as file:
            file.write(f"{self.high_score}")

