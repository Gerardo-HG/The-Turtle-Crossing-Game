from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        """
        Initializes the scoreboard.
        - Sets the color, hides the turtle, and sets the initial level.
        - Updates the scoreboard with the current level.
        """
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard with the current level.
        """
        self.clear()
        self.goto(-380, 300)
        self.write(f"Level : {self.level}", align="left", font=("Ariel", 25, "normal"))

    def update_level(self):
        """
        Increments the level and updates the scoreboard.
        """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Displays the "Game Over" message on the screen.
        """
        self.goto(0, 0)
        self.write("---GAME OVER---", align="center", font=("Ariel", 25, "normal"))
