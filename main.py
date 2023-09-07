from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(snake.up, key="w")
screen.onkey(snake.down, key="s")
screen.onkey(snake.right, key="d")
screen.onkey(snake.left, key="a")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("ate")
        food.refresh()
        scoreboard.hitt()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on=False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

""" for seg_num in range((len(segments) - 1), 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y =segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].fd(10)"""
