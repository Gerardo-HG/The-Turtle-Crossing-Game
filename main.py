from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
import time


screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(800,700)
screen.tracer(0)
screen.listen()

ply = Player()
scr = Scoreboard()
car_bot = Car()


screen.onkey(key="Up",fun=ply.move_up)
screen.onkey(key="Left",fun=ply.move_left)
screen.onkey(key="Right",fun=ply.move_right)


game_is_on = True
while game_is_on:
    time.sleep(car_bot.speed)
    screen.update()
    car_bot.create_cars()
    car_bot.move_cars()

    if ply.ycor() > 320:
        ply.next_level()
        scr.update_level()
        car_bot.next_level()

    #Collisions with cars
    for car in car_bot.cars:
        if ply.distance(car) < 45:
            game_is_on = False
            scr.game_over()

screen.exitonclick()
