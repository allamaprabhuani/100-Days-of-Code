from random import randint
from turtle import Turtle

from scoreboard import Scoreboard

scoreboard = Scoreboard()


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('orange')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        scoreboard.increase_score()
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)

