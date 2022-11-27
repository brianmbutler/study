import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Unfinished

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.move_up,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for cars in range(30):
        car.new_car((random.randint(-260,280),random.randint(-260,280)))
    

screen.exitonclick()