from turtle import Screen
from racket import Racket
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

racket_right = Racket((350, 0))
racket_left = Racket((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(racket_right.up, 'Up')
screen.onkey(racket_right.down, 'Down')

screen.onkey(racket_left.up, 'w')
screen.onkey(racket_left.down, 's')

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.08)
    ball.move()

    # detect colision on the wall top
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounse_y()

    # detect collision with racket
    if (ball.distance(racket_right) < 50 and ball.xcor() > 320) or (ball.distance(racket_left) < 50  and ball.xcor() < - 320):
        ball.bounse_x()

    #detect left missing
    if ball.xcor() == -390:
        score.increase_score_left()
        ball.reset_position()


    #detect right missing
    elif ball.xcor() == 390:
        score.increase_score_right()
        ball.reset_position()


screen.exitonclick()

print("test")