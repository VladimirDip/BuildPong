from turtle import Turtle


class Racket(Turtle):

    def __init__(self, position_racket):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.color('white')
        self.goto(position_racket)
        self.move_distance = 30

    def up(self):
        self.new_y = self.ycor() + self.move_distance
        self.goto(self.xcor(), self.new_y)

    def down(self):
        self.new_y = self.ycor() - self.move_distance
        self.goto(self.xcor(), self.new_y)
