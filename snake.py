from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_new()
        self.head = self.squares[0]

    def create_new(self):
        for cord in COORDINATES:
            self.new_square(cord)

    def new_square(self, cord):
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(cord)
        self.squares.append(new_square)

    def extend(self):
        self.new_square(self.squares[-1].position())

    def move(self):
        for position in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[position - 1].xcor()
            new_y = self.squares[position - 1].ycor()
            self.squares[position].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
