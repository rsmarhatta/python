from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score(self.r_score,self.l_score)


    def right_score(self):
        self.r_score += 1
        self.write_score(self.r_score,self.l_score)
    def left_score(self):
        self.l_score += 1
        self.write_score(self.r_score,self.l_score)
    def write_score(self,scorer,scorel):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))



