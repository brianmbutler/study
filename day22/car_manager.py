from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LOWER_BOUND = -280
UPPER_BOUND = 280


class CarManager(Turtle):
    def __init__ (self):
        super().__init__()
        self.shape('square')
        self.penup()
        
    def new_car(self, position):
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(position)