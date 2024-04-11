from turtle import Turtle


class Game(Turtle):

    def __init__(self, coordinates):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(coordinates)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20.0)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20.0)
