from turtle import Screen
import time
from day23_car import CarManager
from day23_player import Player
from day23_score import Score

screen = Screen()
#screen.bgcolor("white")
screen.setup(width = 600, height = 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)



player = Player()
car_manager = CarManager()
score = Score()

screen.listen()
screen.onkeypress(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move_cars()

    # Detect the collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()



screen.exitonclick()

