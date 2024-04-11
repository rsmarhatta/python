from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()

        self.shapesize(stretch_len= 0.5,stretch_wid= 0.5)
        self.color("red")
        self.speed("fastest")
        self.randomlocation()

    def randomlocation(self):
        random_locX = random.randint(-270,280)
        random_locY = random.randint(-270, 280)
        self.goto(random_locX,random_locY)