from turtle import Turtle

WID = 20
HEIGHT = 100

class Paddle(Turtle):

    X_POSITION = 350
    Y_POSITION = 0

    def __init__(self, position):
        super().__init__()
        self.x_cor, self.y_cor = position
        self.color('white')
        self.shape('square')
        self.penup()
        self.goto(self.x_cor, self. y_cor)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)







