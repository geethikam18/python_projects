import turtle as t
from turtle import Screen

tim = t.Turtle()
screen = Screen()

def move_forwards():
    tim.forward(100)

def move_backwards():
    tim.back(100)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")


screen.exitonclick()




