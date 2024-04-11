# #import turtle
# import random
# from turtle import Turtle, Screen
#
# bobby = Turtle()
# print(bobby)
#
# bobby.shape("turtle")
# bobby.color("DarkOrchid3")
# bobby.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()
#
# # bobby.fillcolor("blue")

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["electric","water","fire"])
table.align = 'l'
table.border = True
print(table)