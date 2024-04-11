import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossy roads 🐥")
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    screen.onkeypress(player.move, "Up")
    car_manager.create_car()
    car_manager.move_cars()
    screen.update()
    # Detect collision with cars moving
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on= False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_lvl()
        car_manager.level_up()


screen.exitonclick()