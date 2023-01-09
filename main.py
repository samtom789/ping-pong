from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.screensize(800,600)
screen.bgcolor('black')
screen.title('PONGOLICIOUS')
screen.tracer(0)

player_1 = Paddle(350,0)
player_2 = Paddle(-350, 0)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(player_1.go_up, 'Up')
screen.onkey(player_1.go_down, 'Down')
screen.onkey(player_2.go_up, 'w')
screen.onkey(player_2.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with wall

    if ball.ycor() > 290 or ball.ycor() < -290:
        #need to bounce
        ball.ybounce()

    #detect when ball contact with paddle
    if ball.distance(player_1) < 50 and ball.xcor() > 330 or ball.distance(player_2) < 50 and ball.xcor() < -330:
        ball.xbounce()

    #detect when ball misses paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.p2_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.p1_point()

screen.exitonclick()
#w = 20, h = 100, x=350, 0. up or down by 20