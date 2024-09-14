from turtle import Turtle
import random as rd
import time

COLORS = ["red", "green", "black", "yellow", "blue", "pink", "brown", "purple", "orange"]
STARTING_MOVE_DISTANCE = 5
INCREMENT_MOVE = 10

class Car(Turtle):
    def __init__(self):
        """
        Initializes the list of cars and sets the initial move distance and speed.
        """
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.speed = 0.1

    def create_cars(self):
        """
        Creates a new car with a chance and adds it to the list of cars.
        """
        chances = rd.randint(1, 6)
        if chances == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(rd.choice(COLORS))
            new_car.shapesize(2, 3)
            new_y = rd.randint(-280, 280)
            new_car.goto(390, new_y)
            self.cars.append(new_car)

    def move_cars(self):
        """
        Moves all cars backward by the defined move distance.
        """
        for car in self.cars:
            car.backward(self.move_distance)

    def next_level(self):
        """
        Hides all cars, increases the move distance, and resets the list of cars.
        """
        for car in self.cars:
            car.hideturtle()
        self.move_distance += INCREMENT_MOVE
        self.cars = []
