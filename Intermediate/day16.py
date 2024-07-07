import day16_module

print(day16_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
# Turtle color change
timmy.color("coral")

# Move turtle by 100 paces
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

