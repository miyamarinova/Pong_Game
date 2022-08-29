from turtle import Turtle

class Points(Turtle):
    ALIGN = 'center'
    FONT = ('Courier', 80, "normal")

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.goto(-140, 200)
        self.write(self.left_player_score, align = self.ALIGN, font=self.FONT)
        self.goto(140, 200)
        self.write(self.right_player_score, align=self.ALIGN, font=self.FONT)

    def left_points(self):
        self.left_player_score += 1
        self.update_score()

    def right_points(self):
        self.right_player_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-140, 200)
        self.write(self.left_player_score, align=self.ALIGN, font=self.FONT)
        self.goto(140, 200)
        self.write(self.right_player_score, align=self.ALIGN, font=self.FONT)


