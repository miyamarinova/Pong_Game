from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from points import Points
screen = Screen()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
points = Points()

screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.listen()
screen.onkey(right_paddle.up, key='Up')
screen.onkey(right_paddle.down, key='Down')

screen.onkey(left_paddle.up, key='w')
screen.onkey(left_paddle.down, key='s')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # this way the ball will move slowly
    screen.update()
    ball.move()
# Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

#Detect if ball goes out of bounds at the edge of the screen
    if ball.xcor() > 380:
        points.left_points()
        ball.start_over()

    if ball.xcor() < -380:
        points.right_points()
        ball.start_over()


screen.exitonclick()