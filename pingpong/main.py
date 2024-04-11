import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from game import Game

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My pingpong game 🏓")
screen.tracer(0)
r_paddle = Game((350, 0))
l_paddle = Game((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    screen.onkeypress(r_paddle.move_up, "Up")
    screen.onkeypress(r_paddle.move_down, "Down")
    screen.onkeypress(l_paddle.move_up, "w")
    screen.onkeypress(l_paddle.move_down, "s")
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # elif ball.ycor() > 280:
    #     ball.reset_position()
    #     scoreboard.right_score()

    # Detecting collision with the paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score()


screen.exitonclick()
