'''
# Draw a 100 x 100 Square

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()


#timmy_the_turtle.forward(100)
#timmy_the_turtle.left(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.left(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.left(90)
#timmy_the_turtle.forward(100)

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()

'''


'''
#Draw a dashed line

from turtle import Turtle, Screen
import turtle as t

tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()


'''

'''

#Drawing different shapes

import turtle as t

import random

tim = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(n):
    angle = 360 / n
    for _ in range(n):
        tim.forward(100)
        tim.left(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

'''

'''

#Draw a random walk

import turtle as t
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = t.Turtle()
tim.pensize(15)
tim.speed(9)
#tim.speed("fastest")

directions = [0, 90, 180, 270]


for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(25)
    tim.setheading(random.choice(directions))

'''

'''


#Generating random RGB Colors

import turtle as t
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



tim.pensize(15)
tim.speed(9)
#tim.speed("fastest")

directions = [0, 90, 180, 270]


for _ in range(200):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(directions))
'''



# Make a spirograph

import turtle as t

import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


print(random_color())
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()












