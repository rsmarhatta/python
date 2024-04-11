# import colorgram
#
#
# colors = colorgram.extract('dothirstimage.jpg', 30)
# listofcolors = []
# #print(colors)
# for color in colors:
#     rgb = (color.rgb.r,color.rgb.g,color.rgb.b) # e.g. (255, 151, 210)
#     listofcolors.append(rgb)
import random
import turtle
from turtle import Turtle, Screen

listofcolors = [(188, 19, 46), (244, 233, 61), (252, 230, 236), (217, 238, 244), (195, 76, 34), (218, 66, 106),
                (15, 142, 89), (196, 176, 19), (21, 125, 173), (108, 182, 209), (18, 167, 213), (209, 153, 90),
                (26, 40, 75), (36, 43, 110), (79, 175, 96), (181, 44, 65), (235, 231, 5), (216, 67, 48),
                (217, 129, 153), (125, 185, 119), (238, 161, 180), (8, 61, 38), (148, 209, 221), (9, 92, 53),
                (6, 87, 109), (160, 30, 27), (237, 169, 162), (159, 212, 183)]
# print(listofcolors)
timmy = Turtle()
timmy.shape("circle")
timmy.speed("fastest")
timmy.hideturtle()
turtle.colormode(255)

y = -290
for i in range(10):
    x = -290
    y += 50
    for j in range(10):
        timmy.penup()
        timmy.goto(x, y)
        timmy.width(20)
        timmy.pendown()
        timmy.begin_fill()
        timmy.dot(20,random.choice(listofcolors))
        timmy.end_fill()
        x += 50

screen = Screen()
screen.exitonclick()
