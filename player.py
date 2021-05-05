from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.gotoStart()
        self.setheading(90)

    def moveForward(self):
        self.forward(MOVE_DISTANCE)

    def gotoStart(self):
        self.setpos(STARTING_POSITION)

    def isAtFinishLine(self):
        if self.ycor() > 280:
            self.gotoStart()
            return True
        return False
