"""Module creating the scoreboard and tracking the score"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Class representing a scoreboard"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        """Method to update the high score and reset the score"""
        self.high_score = max(self.high_score, self.score)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """Display game over when the player loses"""
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by one and update the scoreboard"""
        self.score += 1
        self.update_scoreboard()
