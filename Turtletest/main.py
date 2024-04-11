import math
import turtle
from turtle import Turtle,Screen
import random

timmy = Turtle()
timmy.shape("turtle")



def draw_square():
    for i in range(0,4):
        timmy.forward(100)
        timmy.right(90)

def dashed_line():
    for i in range(50):
        if(i%2==0):
            timmy.penup()
            timmy.forward(5)
        timmy.pendown()
        timmy.forward(5)

def draw_shape(num_sides):

    for j in range (num_sides):
        timmy.right(360/num_sides)
        timmy.forward(100)

def set_random_pencolor():
    turtle.colormode(255)
    timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_walk(steps):

    timmy.width(15)
    directions = [0,90,180,270]

    timmy.speed(10)

    for i in range(steps):
        set_random_pencolor()
        randnum = random.choice(directions)
        timmy.forward(20)
        timmy.setheading(randnum)

# for num_n in range(3,11):
#     set_random_pencolor()
#     draw_shape(num_n)

# draw_square()
# dashed_line()
def draw_spirograph(radius):
    #A = pi*r^2
    #2πr

    timmy.speed("fastest")

    for i in range (int(360/radius)):
        set_random_pencolor()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + radius)


#random_walk(200)
draw_spirograph(5)
screen = Screen()
screen.exitonclick()