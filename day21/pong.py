from turtle import Turtle, Screen, left
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")


is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision with top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    #detect paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()



screen.exitonclick()