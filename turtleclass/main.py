from turtle import Turtle, Screen
import random

is_race_on=False
winner = ''
screen = Screen()

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []
y_val = -150
for index in range(0,6):
    turtle = Turtle("turtle")
    turtle.color(colors[index])
    all_turtles.append(turtle)
    turtle.penup()
    turtle.goto(x=-230, y=y_val)
    y_val +=65

if user_bet:
    is_race_on= True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on= False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The winning turtle was {winner}")
            else:
                print(f"Sorry but the winning turtle was {winner}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()