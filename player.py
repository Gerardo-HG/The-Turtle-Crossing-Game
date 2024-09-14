from turtle import Turtle

STARTING_MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        """
        Initializes a new player.
        - Sets the player's shape, color, and size.
        - Positions the player at the starting location and sets the movement direction.
        """
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.shapesize(2, 2)
        self.initial_x = 0
        self.initial_y = -310
        self.move_distance = STARTING_MOVE_DISTANCE
        self.goto(self.initial_x, self.initial_y)
        self.setheading(90)

    def move_up(self):
        """
        Moves the player up by the defined move distance.
        """
        new_y = self.ycor() + self.move_distance
        self.goto(self.xcor(), new_y)

    def move_left(self):
        """
        Moves the player left by the defined move distance.
        """
        new_x = self.xcor() - self.move_distance
        self.goto(new_x, self.ycor())

    def move_right(self):
        """
        Moves the player right by the defined move distance.
        """
        new_x = self.xcor() + self.move_distance
        self.goto(new_x, self.ycor())

    def next_level(self):
        """
        Resets the player's position to the starting point and increases the move distance for the next level.
        """
        self.goto(self.initial_x, self.initial_y)
        self.move_distance += 5
