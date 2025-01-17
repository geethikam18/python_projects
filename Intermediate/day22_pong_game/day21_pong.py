from turtle import Turtle, Screen
from day21_paddle import Paddle
from day21_ball import Ball
from day21_score import Score


import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()



screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Detect the collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if (ball.distance(right_paddle) < 50 and ball.xcor() < 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()


    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()