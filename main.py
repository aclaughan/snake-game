import logging
from time import sleep
from turtle import Screen, Turtle
from snake import Snake

logging.basicConfig(level = logging.DEBUG)

scr = Screen()
scr.setup(width = 600, height = 600)
scr.bgcolor("black")
scr.title(titlestring = "my snake game")
scr.tracer(0)

snake = Snake()
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



scr.exitonclick()
# logging.debug(stuff)
