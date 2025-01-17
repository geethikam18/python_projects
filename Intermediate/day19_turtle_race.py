from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
screen = Screen()

screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["black", "orange", "yellow", "green", "blue", "purple"]
y_positions = [80, 50, 20, -10, -40, -70]
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape = "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} the turtle is winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





screen.exitonclick()
