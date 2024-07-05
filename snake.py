"""Module creating the snake"""

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Class representing a snake"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Method to create the starting snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Method to add a segment to the snake"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Method to append a segment to the last segment of the snake"""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """Method to reset the snake"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """Method to move each segment of the snake"""
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Method to change the snake's direction UP"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Method to change the snake's direction DOWN"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Method to change the snake's direction LEFT"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Method to change the snake's direction RIGHT"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
