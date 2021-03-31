import logging
from time import sleep
from turtle import Screen, Turtle

logging.basicConfig(level = logging.DEBUG)

game_started = False
scr = Screen()
scr.setup(width = 600, height = 600)
scr.bgcolor("black")
scr.title(titlestring = "my snake game")
scr.tracer(0)

start_pos = [(0,0),(-20, 0), (-40, 0)]

segments = []


for position in start_pos:
    new_sq = Turtle("square")
    new_sq.color("white")
    new_sq.penup()
    new_sq.goto(position)
    segments.append(new_sq)

game_started = True

while game_started:
    scr.update()
    sleep(0.1)

    for seq_num in range(len(segments) -1, 0, -1):
        new_x = segments[seq_num -1].xcor()
        new_y = segments[seq_num -1].ycor()
        segments[seq_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)



scr.exitonclick()
# logging.debug(stuff)
