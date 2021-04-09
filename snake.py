from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE=20


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.snake_head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.squares.append(tim)

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        for segment in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[segment - 1].xcor()
            new_y = self.squares[segment - 1].ycor()
            self.squares[segment].goto(new_x, new_y)
        self.snake_head.forward(MOVING_DISTANCE)

    def pointing_upward(self):
        if(int(self.snake_head.heading()) != 270):
            self.snake_head.setheading(90)


    def pointing_downward(self):
        if (int(self.snake_head.heading()) != 90):
            self.snake_head.setheading(270)


    def pointing_right(self):
        if (int(self.snake_head.heading()) != 180):
            self.snake_head.setheading(0)


    def pointing_left(self):
        if (int(self.snake_head.heading()) != 0):
            self.snake_head.setheading(180)

    def snake_reset(self):
        for seg in self.squares:
            seg.goto(x=-1000, y=1000)
        self.squares = []
        self.create_snake()
        self.snake_head = self.squares[0]

