import logging
from time import sleep
from turtle import Screen
from scoreboard import Scoreboard

from snake import Snake
from food import Food

logging.basicConfig(level = logging.DEBUG)

scr = Screen()
scr.setup(width = 600, height = 600)
scr.bgcolor("black")
scr.title(titlestring = "my snake game")
scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_started = True

while game_started:
    scr.update()
    sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 \
            or snake.head.xcor() < -280 \
            or snake.head.ycor() > 280 \
            or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

scr.exitonclick()
# logging.debug(stuff)
