from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.reset_head()

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def reset_head(self):
        self.head = self.segments[0]

    def add_segment(self, position):
        new_sq = Turtle("square")
        new_sq.color("white")
        new_sq.penup()
        new_sq.goto(position)
        self.segments.append(new_sq)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seq_num - 1].xcor()
            new_y = self.segments[seq_num - 1].ycor()
            self.segments[seq_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.goto(2000,2000)
        self.segments.clear()
        self.create_snake()
        self.reset_head()

