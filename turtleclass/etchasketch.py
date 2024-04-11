from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



def move_forward():
    #tim.setheading(0)
    tim.forward(10)
def move_backwards():
    #.setheading(180)
    tim.backward(10)

def turn_right():
    tim.right(10)
def turn_left():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.setheading(0)
    tim.setposition(0,0)
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backwards,key="s")
screen.onkey(fun=turn_left,key="a")
screen.onkey(fun=turn_right,key="d")
screen.onkey(fun=clear,key="c")
screen.exitonclick()