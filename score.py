from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_right} : {self.score_left}", align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.clear()
        self.score_left += 1
        self.update_scoreboard()

    def increase_score_right(self):
        self.clear()
        self.score_right += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
