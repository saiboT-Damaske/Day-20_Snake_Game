from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    """this initializes a snake with the size of three 20x20 turtles"""

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in STARTING_POS:
            self.add_segment(i)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def add_segment(self, position):
        t1 = Turtle()
        t1.penup()
        t1.shape("square")
        t1.color("white")
        t1.goto(position)
        self.snake.append(t1)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)
