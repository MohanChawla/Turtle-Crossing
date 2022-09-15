from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    # Detect Successful Crossing
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)

