from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    scoreboard.score()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280  or ball.ycor() < -280:
        ball.bounce()

    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()    
    
    if (ball.xcor() > 400):
        scoreboard.left_point()
        ball.game_over()

    if (ball.xcor() < -400):
        scoreboard.right_point()
        ball.game_over()

        
        


screen.exitonclick()