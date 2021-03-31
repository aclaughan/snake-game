from turtle import Turtle
START_POS = [(0,0),(-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake( self ):
        for position in START_POS:
            new_sq = Turtle("square")
            new_sq.color("white")
            new_sq.penup()
            new_sq.goto(position)
            self.segments.append(new_sq)

    def move( self ):
        for seq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seq_num - 1].xcor()
            new_y = self.segments[seq_num - 1].ycor()
            self.segments[seq_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)
