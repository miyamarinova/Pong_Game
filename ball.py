from turtle import Turtle
import random

class Ball(Turtle):
    x_pos = 0
    y_pos = 0

    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.goto(self.x_pos, self.y_pos)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def start_over(self):
        self.penup()
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()